#!/usr/bin/env python3

import typer

from continual.python.cli import utils
from continual.python.sdk.client import Client

from rich.console import Console

app = typer.Typer(help="Manage environments.")


def format_environment_data(e, zipped=False):
    create_time = e.create_time.replace(microsecond=0)
    update_time = e.update_time.replace(microsecond=0)

    c = Client()

    environment_id = e.id
    current_project = utils.get_project(c.config.project)
    current_environment = utils.get_environment(current_project, c.config.environment)

    if (
        "@" not in environment_id
        and current_project.endswith(environment_id)
        and (current_environment in ("production") or not current_environment)
    ):
        environment_id = f"{environment_id} (active)"
    elif e.name == utils.get_environment_name(current_project, current_environment):
        environment_id = f"{environment_id} (active)"

    if zipped:
        data = [
            environment_id,
            e.source,
            e.summary.model_count,
            e.summary.model_version_count,
            e.summary.prediction_count,
            create_time,
            update_time,
        ]
        headers = [
            "ID",
            "Source",
            "Models",
            "Model Versions",
            "Predictions",
            "Created",
            "Updated",
        ]
        return tuple(
            [x[0], x[1]] for x in (zip(headers, data))
        )  # for some reason list(zip) causes issues, so ...
    else:
        data = [
            environment_id,
            e.summary.model_count,
            e.summary.model_version_count,
            e.summary.prediction_count,
            create_time,
            # update_time,
        ]
        headers = [
            "ID",
            "Models",
            "Model Versions",
            "Predictions",
            "Created",
            # "Updated",
        ]
        return (data, headers)


# use callback to run list command if nothing is passed in
@app.callback(invoke_without_command=True)
def default(ctx: typer.Context):
    if ctx.invoked_subcommand is not None:
        return
    else:
        list(n=30, project=None, filters=[], style=None)


@app.command("list")
@utils.exit_on_error
def list(
    project: str = typer.Option(None, help="Project ID."),
    n: int = typer.Option(30, "--num", "-n", help="Number of records to show."),
    style: utils.ContinualStyle = typer.Option(None, help="Color to use for list."),
):
    """List environments."""
    project = utils.get_project(project)
    c = Client(project=project)
    projectObj = c.projects.get(project)
    data = []
    headers = []
    filter_snippet = " (n=%s)" % n
    for e in projectObj.environments.list(n):
        (e_data, headers) = format_environment_data(e)
        data.append(e_data)
    typer.secho(
        "Found %s environments in project %s%s:" % (len(data), project, filter_snippet),
        fg="blue",
    )
    utils.print_table(data, headers, style=utils.get_style(style))


@app.command("get")
@utils.exit_on_error
def get(
    environment: str = typer.Argument(..., help="Environment ID."),
    project: str = typer.Option(None, help="Project ID."),
    json: bool = typer.Option(False, "--json", help="Print full JSON representation."),
):
    """Get environment details."""
    project, environment = utils.get_project_and_environment(project, environment)
    c = Client(project=utils.get_environment_name(project, environment))
    projectObj = c.projects.get(project)

    env = projectObj.environments.get(environment)
    if json:
        console = Console()
        console.print(env.to_dict())
    else:
        data = format_environment_data(env, zipped=True)
        typer.secho("\nRetrieving environment %s: \n" % (environment), fg="blue")
        utils.print_info(data)


@app.command("create")
@utils.exit_on_error
def create(
    environment: str = typer.Argument(..., help="Environment ID."),
    project: str = typer.Option(None, help="Project ID."),
    source: str = typer.Option(
        None,
        "--from",
        help="Project or Environment name from which to create this Environment.",
    ),
):
    """Create environment."""
    project, environment = utils.get_project_and_environment(project, environment)
    c = Client(project=utils.get_environment_name(project, environment))
    projectObj = c.projects.get(project)
    try:
        env = projectObj.environments.create(id=environment, source=source)
        typer.secho("Successfully created environment %s." % env.name, fg="green")
    except Exception as e:
        typer.secho(
            "Failed to create environment %s in project %s: %s"
            % (environment, project, str(e)),
            fg="red",
        )


@app.command("delete")
@utils.exit_on_error
def delete(
    environment: str = typer.Argument(..., help="Environment ID."),
    project: str = typer.Option("", help="Project ID."),
    force: bool = typer.Option(
        False, "--force", help="Force deletion. Skips confirmation."
    ),
):
    """Delete environment."""
    project, environment = utils.get_project_and_environment(project, environment)
    c = Client(project=utils.get_environment_name(project, environment))
    projectObj = c.projects.get(project)

    if not force:
        force = typer.confirm(
            "Are you sure you want to delete environment %s in project %s? This will delete all resources in the environment."
            % (environment, project)
        )
    if force:
        env = projectObj.environments.get(environment)
        env.delete()
        if c.config.environment == environment and c.config.project == project:
            typer.secho(
                "Since (%s) was the active environment in the active project, the active environment was switched to production."
                % environment,
                fg="blue",
            )
            c.config.set_environment("production")
        typer.secho(
            "Successfully deleted environment %s in project %s."
            % (environment, project),
            fg="green",
        )
    else:
        typer.secho("Environment deletion cancelled! ", fg="green")


@app.command("update")
@utils.exit_on_error
def update(
    environment: str = typer.Argument(..., help="environment ID."),
    project: str = typer.Option(None, help="Project ID."),
    scheduling_enabled: bool = typer.Option(
        False, "--scheduling-enabled", help="Is scheduling enabled in the environment?"
    ),
    database: str = typer.Option(
        None,
        "--db",
        help="Database to use for environment. Default is the same database as production.",
    ),
    schema: str = typer.Option(
        None,
        help="Schema to use for environment. Default is to postfix the production schema by this environment name.",
    ),
):
    """Update environment name, database, or schema."""
    project, environment = utils.get_project_and_environment(project, environment)
    c = Client(project=utils.get_environment_name(project, environment))
    projectObj = c.projects.get(project)

    env = projectObj.environments.get(environment)
    try:
        if schema is not None or database is not None:
            fs_type = env.data_store.type
            conn_info = {}
            if database:
                conn_info["database"] = database
            if schema:
                if fs_type == "big_query":
                    conn_info["dataset"] = schema
                else:
                    conn_info["db_schema"] = schema
            data_store = {"type": fs_type}
            data_store[fs_type] = conn_info
            env.update(scheduling_enabled=scheduling_enabled, data_store=data_store)
        else:
            env.update(scheduling_enabled=scheduling_enabled)
        typer.secho(
            "Successfully updated environment %s in project %s."
            % (environment, project),
            fg="green",
        )
    except Exception as e:
        typer.secho(
            "Failed to update environment %s in project %s: %s"
            % (environment, project, str(e)),
            fg="red",
        )
