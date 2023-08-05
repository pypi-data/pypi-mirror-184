"""List-members CLI command definition."""
import sys
from typing import List
from typing import Optional

import typer
from returns.pipeline import flow
from returns.pointfree import alt
from returns.pointfree import bind
from returns.pointfree import map_
from rich.console import Console
from rich.style import Style
from rich.table import Table

from dapla_team_cli.config import DAPLA_TEAM_API_BASE
from dapla_team_cli.groups.list_members.models import Group
from dapla_team_cli.groups.list_members.models import Team
from dapla_team_cli.groups.list_members.models import User
from dapla_team_cli.groups.list_members.models import get_resource
from dapla_team_cli.groups.services.list_groups import deduce_team_info
from dapla_team_cli.tf.iam_bindings import MissingUserSuppliedInfoError


console = Console()

styles = {
    "normal": Style(blink=True, bold=True),
    "warning": Style(color="dark_orange3", blink=True, bold=True),
}


def fail(message: str) -> None:
    """Exit with a message if a Failure occurs."""
    print(message)
    sys.exit(1)


def list_members(
    team_name: Optional[str] = typer.Option(None, "--team-name", "-tn", help="Team name (e.g. demo-enhjoern-a)")  # noqa: B008
) -> None:
    """List groups (and members) for a team."""
    if not team_name:
        team = deduce_team_info()
        team_name = team.name

    if not team_name:
        raise MissingUserSuppliedInfoError("Not a IaC repo and no team_name supplied, nothing to do...")

    flow(
        f"{DAPLA_TEAM_API_BASE}/teams/{team_name}",
        get_resource,
        map_(Team.parse_obj),
        bind(Team.groups),
        map_(_print_groups),
        alt(fail),
    )


def _print_groups(groups: List[Group]) -> None:
    for group in groups:
        members_list = group.users().alt(fail).unwrap()
        group_name = group.ID

        if members_list:
            _print_table(members_list, group_name)


def _add_row(member: User, table: Table) -> Table:
    """Adds a Member; name and shortform email to a row in a table.

    Args:
        member: Dapla team member to add
        table: Table to store the new row inn.

    Returns:
        Table used to add more rows or to draw to console
    """
    name = f"[b]{member.name}[/b]"
    table.add_row(f"[b]{name}[/b]", f"[b]{member.email_short}[/b]")

    return table


def _print_table(members: List[User], team_name: str) -> Table:
    """Makes a table and prints it to console.

    Adds columns for all member attributes, adds team name as title and
    calls _add_row on every member to add rows with member their information.

    Args:
        members: List of Dapla team member to add
        team_name: Dapla team name and auth group combined (e.g. demo-enhjoern-a-support).

    Returns:
        Table, that was used to print
    """
    table = Table(title=f"\n[b]{team_name}[/b]")
    table.add_column("[b]Name[/b]", justify="left")
    table.add_column("[b]Email[/b]", justify="left")
    table.min_width = 100

    for member in members:
        _add_row(member, table)

    console.print(table)
    return table
