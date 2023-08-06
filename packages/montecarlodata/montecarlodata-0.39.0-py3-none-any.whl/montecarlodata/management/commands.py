import click

from montecarlodata.common import create_mc_client
from montecarlodata.management.service import ManagementService


@click.group(help="Manage account settings.")
def management():
    """
    Group for any management related subcommands
    """
    pass


@management.command(help="Get PII filtering preferences.")
@click.pass_obj
def get_pii_preferences(ctx):
    ManagementService(mc_client=create_mc_client(ctx)).get_pii_preferences()


@management.command(help="Configure PII filtering preferences for the account.")
@click.option(
    "--enable/--disable",
    "enabled",
    required=False,
    type=click.BOOL,
    default=None,
    help="Whether PII filtering should be active for the account.",
)
@click.option(
    "--fail-mode",
    required=False,
    type=click.Choice(["CLOSE", "OPEN"], case_sensitive=False),
    help="Whether PII filter failures will allow (OPEN) or prevent (CLOSE) data flow for this account.",
)
@click.pass_obj
def configure_pii_filtering(ctx, **kwargs):
    ManagementService(mc_client=create_mc_client(ctx)).set_pii_filtering(**kwargs)
