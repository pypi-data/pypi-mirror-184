from __future__ import annotations

from datetime import datetime

import isolate_cloud.auth as auth
import typer
from isolate_cloud import sdk
from rich.console import Console
from rich.table import Table

console = Console()
cli = typer.Typer()

auth_cli = typer.Typer()


@auth_cli.command(name="login")
def auth_login():
    auth.login()


@auth_cli.command(name="logout")
def auth_logout():
    auth.logout()


@auth_cli.command(name="hello", hidden=True)
def auth_test():
    """
    To test auth.
    """
    print(f"Hello, {auth.USER.info['name']}")


key_cli = typer.Typer()


@key_cli.command(name="generate")
def key_generate(host: str = "localhost", port: str = "6005"):
    connection = sdk.FalCloudClient(f"{host}:{port}").connect()
    result = connection.create_user_key()
    print(
        "Generated key id and key secret.\n"
        "This is the only time the secret will be visible.\n"
        "You will need to generate a new key pair if you lose access to this secret."
    )
    print(f"KEY_ID='{result[1]}'\nKEY_SECRET='{result[0]}'")


@key_cli.command(name="list")
def key_list(host: str = "localhost", port: str = "6005"):
    connection = sdk.FalCloudClient(f"{host}:{port}").connect()
    keys = connection.list_user_keys()
    for key in keys:
        print(f"KEY_ID='{key.key_id}' @ {key.created_at.ToDatetime()}")
    else:
        print("No more keys.")


@key_cli.command(name="revoke")
def key_revoke(key_id: str, host: str = "localhost", port: str = "6005"):
    connection = sdk.FalCloudClient(f"{host}:{port}").connect()
    connection.revoke_user_key(key_id)


scheduled_cli = typer.Typer()


@scheduled_cli.command(name="list")
def list_scheduled(host: str = "localhost", port: str = "6005"):
    table = Table(title="Scheduled jobs")
    table.add_column("Job ID")
    table.add_column("State")
    table.add_column("Cron")

    client = sdk.FalCloudClient(f"{host}:{port}")
    with client.connect() as connection:
        for cron in connection.list_scheduled_runs():
            table.add_row(cron.run_id, cron.state.name, cron.cron)

    console.print(table)


@scheduled_cli.command(name="activations")
def list_activations(
    job_id: str,
    host: str = "localhost",
    port: str = "6005",
    limit: int = 15,
):
    table = Table(title="Job activations")
    table.add_column("Job ID")
    table.add_column("Activation ID")
    table.add_column("Activation Date")

    client = sdk.FalCloudClient(f"{host}:{port}")
    with client.connect() as connection:
        for cron in connection.list_run_activations(job_id)[-limit:]:
            table.add_row(
                cron.run_id,
                cron.activation_id,
                str(datetime.fromtimestamp(int(cron.activation_id))),
            )

    console.print(table)


@scheduled_cli.command(name="logs")
def print_logs(
    job_id: str,
    activation_id: str,
    host: str = "localhost",
    port: str = "6005",
):
    client = sdk.FalCloudClient(f"{host}:{port}")
    with client.connect() as connection:
        raw_logs = connection.get_activation_logs(
            sdk.ScheduledRunActivation(job_id, activation_id)
        )
        console.print(raw_logs.decode(errors="ignore"), highlight=False)


@scheduled_cli.command("cancel")
def cancel_scheduled(job_id: str, host: str = "localhost", port: str = "6005"):
    client = sdk.FalCloudClient(f"{host}:{port}")
    with client.connect() as connection:
        connection.cancel_scheduled_run(job_id)
        console.print("Cancelled", repr(job_id))


cli.add_typer(auth_cli, name="auth")
cli.add_typer(key_cli, name="key")
cli.add_typer(scheduled_cli, name="scheduled")

if __name__ == "__main__":
    cli()
