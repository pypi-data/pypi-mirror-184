# Copyright (c) 2021, InOrbit, Inc.
# All rights reserved.
import json
import logging
import os
import sys
from datetime import datetime

import click
import inorbit.exceptions
import yaml
from inorbit import client
from tabulate import tabulate

logger = logging.getLogger(__name__)
logging_handler = logging.StreamHandler(sys.stderr)
logging_handler.setFormatter(logging.Formatter("%(levelname)s %(funcName)s:%(lineno)d %(message)s"))
logger.addHandler(logging_handler)

client.set_logger(logger)


def display_response_messages(response, index=None):
    """
    Processes any results sent as part of the response inclued in HTTP API calls

    Args:
     - response is a requests.Response object
     - index is a number identifying which configuration object was being applied
    """

    try:
        response_object = response.json()
        if response_object and response_object["messages"]:
            for m in response_object["messages"]:
                fg_color = None
                # colorize the message if it is an error or warning
                message = m.get("message") if type(m) is dict and "message" in m else m
                level = m.get("level") if type(m) is dict and "level" in m else None
                if level == "WARN" or level == "warn":
                    fg_color = "yellow"
                elif level == "ERROR" or level == "error":
                    fg_color = "red"
                if message:
                    styled_msg = click.style(message, fg=fg_color)
                    click.echo(f"[{index}] " + styled_msg if index is not None else styled_msg)
    except Exception as _:
        pass  # Ignore - not a JSON response


def get_id_to_name_mapping(resource_name):
    """Returns a dictionary mapping resource id to resource name

    Args:
        resource_name (string): name of the resource to generate the mapping

    Returns:
        dict: dictionary mapping resource id to resource name
    """

    endpoint_raw_response = client.http_get(f"/{resource_name}").json()
    resource_id_to_name_mapping = {res["id"]: res["name"] for res in endpoint_raw_response}
    return resource_id_to_name_mapping


# This is the CLI entrypoint. It's hooked by `setup.py` (see `entry_points` parameter).
@click.group()
@click.option("--verbose", default=False, is_flag=True)
def cli(verbose):
    """InOrbit Command Line Interface tool

    The InOrbit CLI tool enable roboteers to interact
    with the InOrbit Cloud platform in order to manage
    robot configuration as code.
    """

    if verbose or "INORBIT_CLI_VERBOSE" in os.environ:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.ERROR)


@cli.group()
def get():
    """Get objects basic information."""
    pass


@cli.group()
def expr():
    """Commands related to expressions."""
    pass


@cli.group()
def describe():
    """Describe objects and provide detailed information."""
    pass


@cli.group(name="list")
def list_configs():
    """Lists possible values for a given option"""
    pass


@cli.group(invoke_without_command=True)
@click.option("-f", "filename", type=click.Path(exists=True, resolve_path=True))
@click.pass_context
def delete(ctx, filename):
    """Delete an object by id or by providing a configuration file."""

    # `delete` is used both as a command and as a command group. The command
    # accepts an option that is required but we cannot enforce it because other
    # commands under the `delete` group (e.g. `inorbit delete config foo`) fails.

    # Handle missing filename option. If there's invoked subcommand, it means
    # the `delete` was called with no option, so we show help and return.
    # If this gets executed as a callback for a subcommand, just ignore it.
    if not filename:
        if not ctx.invoked_subcommand:
            click.echo(ctx.get_help())
        return

    logger.debug(f"Reading file '{click.format_filename(filename)}'")

    # $ inorbit config delete -f sample_config.json
    # Load all configs in the file. This buffers all contents in memory and is not efficient,
    # it could be streamed more easily -- but it is preferrable to parse the entire contents
    # and fail early in case there are parsing errors in later documents.
    with open(file=filename, mode="r") as fd:
        config_objects_list = list(yaml.load_all(fd, Loader=yaml.FullLoader))
        # If the file is a JSON, the above function could return a list with the first element
        # being a list of config objects inside
        # so we are only taking the first element of the list, that should be a list
        if len(config_objects_list) == 1 and isinstance(config_objects_list[0], list):
            config_objects_list = config_objects_list[0]

    logger.debug(config_objects_list)
    for config_object in config_objects_list:
        required_keys = ["kind", "apiVersion", "metadata"]
        delete_config = {k: config_object[k] for k in required_keys}

        logger.debug(f"Object required data: {delete_config}")

        index = 0
        try:
            logger.debug("Clearing configuration")
            response = client.http_post("/configuration/clear", post_data=delete_config)
            display_response_messages(response, index)
        except inorbit.exceptions.InOrbitError as ex:
            raise click.ClickException(ex)
        index += 1

    click.echo(f"Configuration {filename} deleted successfully.")


@click.command(name="tags")
def get_tags():
    """Get all tags and relevant tag data."""
    response = client.http_get("/tags").json()
    response = [
        {
            "name": r["name"],
            "id": r["id"],
            "description": r.get("description", ""),
        }
        for r in response
    ]
    click.echo(tabulate(response, headers="keys"))


get.add_command(get_tags)


@click.command(name="collections")
def get_collections():
    """
    Get all collections and relevant collection data.

    Instead of showing all tags associated to a particular collection,
    it only shows the number of tags under each collection. To get more
    detailed data about collections use `describe_collections`.
    """

    response = client.http_get("/collections").json()
    response = [
        {
            "name": r["name"],
            "id": r["id"],
            "tags count": len(r["tags"]),
        }
        for r in response
    ]
    click.echo(tabulate(response, headers="keys"))


get.add_command(get_collections)


@click.command(name="robots")
def get_robots():
    """Get all robots and relevant robot data."""
    response = client.http_get("/robots").json()
    response = [
        {
            "name": r["name"],
            "id": r["id"],
            "agent version": r.get("agentVersion", ""),
        }
        for r in response
    ]
    click.echo(tabulate(response, headers="keys"))


get.add_command(get_robots)


@click.command(name="tags")
def describe_tags():
    """
    Describe all tags and detailed tag data.

    It also gathers the collection names so the collection id a tag is
    associated to it not shown alone.
    """

    # generate a `collection id` to `collection name` mapping to show
    # the collection name the tag is associated to.
    collection_id_to_name_mapping = get_id_to_name_mapping("collections")

    tags_raw_response = client.http_get("/tags").json()
    response = [
        {
            "name": r["name"],
            "description": r.get("description", ""),
            "collection id": r["collectionId"],
            "collection name": collection_id_to_name_mapping[r["collectionId"]],
        }
        for r in tags_raw_response
    ]

    click.echo(tabulate(response, headers="keys"))


describe.add_command(describe_tags)


@click.command(name="collections")
def describe_collections():
    """Describe all collections and detailed collection data."""
    collections_raw_response = client.http_get("/collections").json()
    for collection in collections_raw_response:
        click.echo(f"Collection '{collection['name']}' has {len(collection['tags'])} tags")
        collection_tags = [
            {"tag name": collection_tag["name"], "tag id": collection_tag["id"]}
            for collection_tag in collection["tags"]
        ]
        # Here `rst` table format has better appeareance and helps to understand
        # the data better. Consider using the same format for all `tabulate` calls.
        click.echo(tabulate(collection_tags, headers="keys", tablefmt="rst"))
        click.echo()


describe.add_command(describe_collections)


@click.command(name="robots")
def describe_robots():
    """Describe all robots and detailed robot data."""
    response = client.http_get("/robots").json()
    response = [
        {
            "name": r["name"],
            "id": r["id"],
            "agent version": r.get("agentVersion", ""),
            "online": r["agentOnline"],
            # TODO: decide which is the best date format and refactor to allow
            # changing it for all outputs or as a command parameter
            "last seen": datetime.fromtimestamp(r["updatedTs"] / 1000).isoformat(),
        }
        for r in response
    ]
    click.echo(tabulate(response, headers="keys"))


describe.add_command(describe_robots)


@click.command(name="apply")
@click.option("-f", "filename", required=True, type=click.Path(exists=True, resolve_path=True))
def apply_config(filename):
    """Apply configuration read from file."""
    logger.debug(f"Reading file '{click.format_filename(filename)}'")

    # Load all configs in the file. This buffers all contents in memory and is not efficient,
    # it could be streamed more easily -- but it is preferrable to parse the entire contents
    # and fail early in case there are parsing errors in later documents.
    with open(file=filename, mode="r") as fd:
        config_objects_list = list(yaml.load_all(fd, Loader=yaml.FullLoader))
        # If the file is a JSON, the above function returns a list with a list inside
        # so we are only taking the first element of the list, that should be a list
        if len(config_objects_list) == 1 and isinstance(config_objects_list[0], list):
            config_objects_list = config_objects_list[0]

    logger.debug(config_objects_list)
    index = 0
    for config_object in config_objects_list:
        try:
            logger.info("Applying configuration")
            response = client.http_post("/configuration/apply", post_data=config_object)
            display_response_messages(response, index)
        except inorbit.exceptions.InOrbitError as ex:
            raise click.ClickException(ex)
        index += 1

    click.echo(f"Configuration {filename} applied successfully.")


# TODO: consider moving apply_config to CLI `config` group
# to unify UX e.g. `inorbit config apply`, `inorbit config list`
# (lean/mike) after first discussion we decided to use `$ inorbit apply -f`, `$ inorbit delete -f`
cli.add_command(apply_config)


@click.command(name="config")
@click.option(
    "--kind",
    "kind",
    type=str,
    required=True,
    help="Configuration kind.",
)
@click.option("--scope", "scope", type=str, default="*", help="Configuration object scope.")
# We should remove the "--dump" parameter in favor of "--json"
@click.option(
    "--dump",
    "is_dump",
    is_flag=True,
    help="(Deprecated: use --json) Dumps full objects to standard output in JSON format.",
)
@click.option(
    "--json",
    "is_json",
    is_flag=True,
    help="Dumps full objects to standard output in JSON format.",
)
@click.option(
    "--yaml",
    "is_yaml",
    is_flag=True,
    help="Dumps full objects to standard output in YAML format.",
)
@click.option(
    "--summary",
    "is_summary",
    is_flag=True,
    help="Dumps a table with resuls with summary info.",
)
@click.option(
    "--include-system-defaults/--no-system-defaults",
    "include_system_defaults",
    default=False,
    help='Deprecated: use "--all". Includes definitions from the system defaults level '
    + '("root" scope).',
)
@click.option(
    "--all",
    "include_all",
    is_flag=True,
    default=False,
    help='Includes elements normally hidden from output (system defaults from "root" scope, '
    + "data sources existing as part of other definitions).",
)
@click.argument("config_id", type=str, required=False)
def get_config(
    kind,
    scope,
    is_dump,
    is_json,
    is_yaml,
    is_summary,
    config_id,
    include_system_defaults,
    include_all,
):
    """List all configurations."""
    if is_dump:
        print('Argument "--dump" is deprecated and will be removed in the future: use "--json"')
    if include_system_defaults:
        print(
            'Argument "--include-system-defaults" is deprecated and will be removed in the '
            + 'future: use "--all"'
        )
    # "--dump" is deprecated should be replaced by "--json" soon. For now, use them as synonyms
    is_json = is_json or is_dump
    if is_json + is_yaml + is_summary > 1:  # these three are mutually exclusive
        raise click.BadParameter("Only one of --dump, --yaml and --summary can be specified")
    full_objects = is_json or is_yaml
    query_data = {"kind": kind, "scope": scope, "format": "full" if full_objects else "short"}
    # configuration ID is optional, so if it's provided we add it as query parameter.
    if config_id:
        query_data["id"] = config_id
    if include_all:
        query_data["all"] = "true"

    try:
        response = client.http_get(
            path="/configuration/list",
            query_data=query_data,
        ).json()
    except inorbit.exceptions.InOrbitError as ex:
        raise click.ClickException(ex)

    if full_objects:  # JSON or YAML format, both require the same processing
        items = [
            r
            for r in response["items"]
            if include_all or include_system_defaults or r["metadata"]["scope"][:5] != "root/"
        ]
        if is_json:  # flag used for JSON form
            print(json.dumps(items, indent=2))
        else:
            print(yaml.dump_all(items))
        return

    response = [
        {
            "id": r["id"],
            "kind": r["kind"],
            "label": r["label"] if "label" in r else None,
            "scope": r["scope"],
            "suppressed": r.get("suppressed", False),
        }
        for r in response["items"]
        if include_system_defaults or r["scope"][:5] != "root/"
    ]
    click.echo(tabulate(response, headers="keys"))


get.add_command(get_config)


@click.command(name="config")
@click.argument("config_id", type=str)
@click.option(
    "--kind",
    "kind",
    type=str,
    required=True,
    help="Configuration kind.",
)
@click.option("--scope", "scope", type=str, default="account", help="Configuration object scope.")
def delete_config(config_id, kind, scope):
    """Clear configuration with the provided id. The default `account` scope
    can be overwritten by providing the `--scope` option."""

    response = client.http_post(
        path="/configuration/clear",
        post_data={
            "kind": kind,
            "apiVersion": "v0.1",
            "metadata": {"id": config_id, "scope": scope},
        },
    ).json()

    logger.debug(response)

    # TODO: improve response
    display_response_messages(response)
    click.echo("OK")


delete.add_command(delete_config)


@click.command(name="eval")
@click.option("-f", "--filename", type=click.Path(exists=True))
@click.argument("robot_id", type=str)
@click.argument("expression", type=str, required=False)
def eval_expression(robot_id, expression, filename):
    """
    Evaluates an expression on a robot.

    The expression is received either as an optional argument, or within a JSON/YAML file with
    format:

    { expression: str, attributes: { attr1: value1, attr2: value2... } }
    """
    if expression:
        # Expression passed from command line; the file option cannot be used
        if filename:
            raise click.BadParameter("Only one of '--filename' and expression is accepted")
        post_data = {"expression": expression}
    elif filename:
        # No expression: A file should be used. Load its contents and pass it directly to REST API
        with open(file=filename, mode="r") as fd:
            post_data = yaml.load(fd, Loader=yaml.FullLoader)
    else:
        raise click.BadParameter("One of '--filename' and expression must be provided")
    response = client.http_post(
        path=f"/expressions/robot/{robot_id}/eval", post_data=post_data
    ).json()
    print(response)


expr.add_command(eval_expression)


@click.command(name="kinds")
def get_kinds():
    """lists all possible kinds."""
    # TODO (Elvio): get the Kinds from an API
    # Using dictionaries in case we want to add "description" or a new field in the table
    kinds = [
        {"name": "StatusDefinition"},
        {"name": "IncidentDefinition"},
        {"name": "ActionDefinition"},
        {"name": "RobotCamera"},
    ]
    click.echo(tabulate(kinds, headers="keys"))
    click.echo(
        "\nLearn more about kinds at: "
        + "https://developer.inorbit.ai/docs?hsLang=en#getting-started-with-the-cli"
    )


list_configs.add_command(get_kinds)
