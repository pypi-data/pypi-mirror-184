from typing import Optional

import click
from pycarlo.core import Client, Mutation, Query
from tabulate import tabulate

from montecarlodata.common.common import ConditionalDictionary
from montecarlodata.errors import manage_errors


class ManagementService:
    _LIST_PII_PREFERENCES_HEADERS = ["Status", "Fail Mode"]

    def __init__(self, mc_client: Optional[Client] = None):
        self._abort_on_error = True
        self._mc_client = mc_client or Client()

    @manage_errors
    def get_pii_preferences(
        self,
        headers: Optional[str] = "firstrow",
        table_format: Optional[str] = "fancy_grid",
    ) -> None:
        table = [self._LIST_PII_PREFERENCES_HEADERS]

        query = Query()
        query.get_pii_filtering_preferences()
        preferences = self._mc_client(query).get_pii_filtering_preferences
        table.append(
            [
                "Enabled" if preferences.enabled else "Disabled",
                preferences.fail_mode,
            ]
        )
        click.echo(tabulate(table, headers=headers, tablefmt=table_format))

    @manage_errors
    def set_pii_filtering(
        self,
        enabled: Optional[bool] = None,
        fail_mode: Optional[str] = None,
    ) -> None:
        variables = ConditionalDictionary(lambda x: x is not None)
        variables.update({"enabled": enabled, "fail_mode": fail_mode})

        mutation = Mutation()
        mutation.update_pii_filtering_preferences(**variables)
        result = self._mc_client(mutation).update_pii_filtering_preferences
        if result.success:
            click.echo("PII filtering preferences have been updated!")
