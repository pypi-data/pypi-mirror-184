import base64
import logging
import sys

import click

from seda import exceptions
from seda.utils import get_app

logger = logging.getLogger("seda")


@click.group()
@click.option("--a", "-A", "path", required=True)
@click.option(
    "--app-dir",
    default=".",
    show_default=True,
    help="Look for APP in the specified directory.",
)
@click.pass_context
def cli(ctx: click.Context, path: str, app_dir: str) -> None:
    sys.path.insert(0, app_dir)
    try:
        ctx.obj = get_app(path)
    except exceptions.ImportPathError as exc:
        logger.error(f"Error loading app. {exc}")
        sys.exit(1)


@cli.command()
@click.pass_context
@click.option(
    "--function",
    "-f",
    "function_name",
    help="AWS Lambda function name.",
)
def deploy(ctx: click.Context, function_name: str) -> None:
    if not function_name and ctx.obj.config.function_name is None:
        logger.error("Function name is required.")
        sys.exit(1)

    with ctx.obj.config.set_function_name(function_name):
        topic_name = ctx.obj.config.get_sns_topic_name()
        click.echo(f"Creating sns topic <@topic {topic_name}>...")
        ctx.obj.create_sns_topic()

        click.echo("Creating sns subscription...")
        ctx.obj.sns_subscribe()

        click.echo("Adding sns permission...")
        try:
            ctx.obj.add_sns_permission()
        except exceptions.AlreadyExistsError:
            pass

        try:
            ctx.obj.delete_schedule_group()
        except exceptions.AlreadyDeletedError:
            pass

        schedule_role_name = ctx.obj.config.get_schedule_role_name()
        click.echo(f"Creating schedule role <@role {schedule_role_name}>...")
        try:
            ctx.obj.create_schedule_role()
        except exceptions.AlreadyExistsError:
            pass

        function_policy_name = ctx.obj.config.get_function_policy_name()
        click.echo(f"Creating lambda policy <@policy {function_policy_name}>...")
        try:
            ctx.obj.put_function_policy()
        except exceptions.AlreadyExistsError:
            pass

        schedule_group_name = ctx.obj.config.get_schedule_group_name()
        click.echo(f"Creating schedule group <@group {schedule_group_name}>...")
        try:
            ctx.obj.create_schedule_group()
        except exceptions.AlreadyExistsError:
            pass

        schedule_group_name = ctx.obj.config.get_schedule_group_name(onetime=True)
        click.echo(f"Creating schedule group <@group {schedule_group_name}>...")
        try:
            ctx.obj.create_schedule_group(onetime=True)
        except exceptions.AlreadyExistsError:
            pass

        click.echo("Scheduling...")
        for schedule in ctx.obj.schedules:
            click.echo(f" + {repr(schedule)}")
            ctx.obj.create_schedule(schedule)


@cli.command()
@click.pass_context
@click.option(
    "--function",
    "-f",
    "function_name",
    help="AWS Lambda function name.",
)
def remove(ctx: click.Context, function_name: str) -> None:
    if not function_name and ctx.obj.config.function_name is None:
        logger.error("Lambda function is required.")
        sys.exit(1)

    with ctx.obj.config.set_function_name(function_name):
        click.echo("Deleting sns permission...")
        try:
            ctx.obj.remove_sns_permission()
        except exceptions.AlreadyDeletedError:
            pass

        topic_name = ctx.obj.config.get_sns_topic_name()
        click.echo(f"Deleting sns topic <@topic {topic_name}>...")
        ctx.obj.delete_sns_topic()

        schedule_group_name = ctx.obj.config.get_schedule_group_name()
        click.echo(f"Deleting schedule group <@group {schedule_group_name}>...")
        try:
            ctx.obj.delete_schedule_group()
        except exceptions.AlreadyDeletedError:
            pass

        # TODO: --all
        schedule_group_name = ctx.obj.config.get_schedule_group_name(onetime=True)
        click.echo(f"Deleting lambda group <@group {schedule_group_name}>...")
        try:
            ctx.obj.delete_schedule_group(onetime=True)
        except exceptions.AlreadyDeletedError:
            pass

        schedule_role_name = ctx.obj.config.get_schedule_role_name()
        click.echo(f"Deleting schedule role <@role {schedule_role_name}>...")
        try:
            ctx.obj.delete_schedule_role()
        except exceptions.AlreadyDeletedError:
            pass

        function_policy_name = ctx.obj.config.get_function_policy_name()
        click.echo(f"Deleting lambda policy <@policy {function_policy_name}>...")
        try:
            ctx.obj.delete_function_policy()
        except exceptions.AlreadyDeletedError:
            pass


@cli.command()
@click.pass_context
@click.option(
    "--function",
    "-f",
    "function_name",
    help="AWS Lambda function name.",
)
@click.argument("command", nargs=1)
def python(ctx: click.Context, function_name: str, command: str) -> None:
    if not function_name and ctx.obj.config.function_name is None:
        logger.error("Lambda function is required.")
        sys.exit(1)

    response = ctx.obj.client.invoke_function(
        function_name,
        payload={"python": command},
    )
    log = base64.b64decode(response["LogResult"]).decode()
    click.echo(log.strip().replace("\t", "\n - "))


@cli.command()
@click.pass_context
@click.option(
    "--function",
    "-f",
    "function_name",
    help="AWS Lambda function name.",
)
@click.argument("command", nargs=1)
def cmd(ctx: click.Context, function_name: str, command: str) -> None:
    if not function_name and ctx.obj.config.function_name is None:
        logger.error("Lambda function is required.")
        sys.exit(1)

    response = ctx.obj.client.invoke_function(
        function_name,
        payload={"cmd": command},
    )
    log = base64.b64decode(response["LogResult"]).decode()
    click.echo(log.strip().replace("\t", "\n - "))


if __name__ == "__main__":
    cli()
