"""Common models and functionality related to Dapla teams members."""
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import requests
from pydantic import BaseModel
from pydantic import Field
from pydantic import parse_obj_as
from returns.result import Failure
from returns.result import Result
from returns.result import Success

from dapla_team_cli.auth.services.get_token import get_token


def get_resource(
    endpoint: str,
) -> Result[Dict[str, Any], str]:
    """Get a given resource (Team/Group/User/a list) from the API."""
    token = get_token()

    try:
        response = requests.get(
            endpoint,
            headers={
                "Authorization": f"Bearer {token}",
            },
            timeout=10,
        )
    except Exception:
        return Failure("Something went wrong trying to access the API")

    if response.status_code != 200:
        return Failure(f"Error trying to access {endpoint}: {response.status_code} {response.reason}")

    return Success(response.json())


class Link(BaseModel):
    """A Link resource in the API."""

    href: str


class User(BaseModel):
    """Information about a Dapla team member.

    Attributes:
        name: Display name from ad, such as `Nordmann, Ola`
        email: Email, such as `noo@ssb.no`
    """

    name: str
    email_short: str = Field(alias="emailShort")
    email: Optional[str]
    links: Dict[str, Link] = Field(alias="_links")


def parse_users(users: Dict[str, Any]) -> List[User]:
    """Parse JSON into a list of Members."""
    if "_embedded" not in users or "userList" not in users["_embedded"]:
        return []
    return parse_obj_as(List[User], users["_embedded"]["userList"])


def get_full_name(self: User) -> str:
    """Get the full name of Member.

    Args:
        self: This members full name.

    Returns:
        Full name of this member.
    """
    return self.name


class Group(BaseModel):
    """Information about a Dapla team auth group."""

    ID: str = Field(alias="id")
    azure_id: str = Field(alias="azureId")
    name: str
    links: Dict[str, Link] = Field(alias="_links")

    def users(self) -> Result[List[User], str]:
        """Get a list of Users in this group."""
        return get_resource(self.links["users"].href).map(parse_users)


def parse_groups(groups_json: Dict[str, Any]) -> List[Group]:
    """Parse JSON into a list of Groups."""
    if "_embedded" not in groups_json or "groupList" not in groups_json["_embedded"]:
        return []
    return parse_obj_as(List[Group], groups_json["_embedded"]["groupList"])


class Team(BaseModel):
    """Information about a Dapla team."""

    uniform_team_name: str = Field(alias="uniformTeamName")
    display_team_name: str = Field(alias="displayTeamName")
    repo: str
    links: Dict[str, Link] = Field(alias="_links")

    def users(self) -> Result[List[User], str]:
        """Get a list of users in this team."""
        return get_resource(self.links["users"].href).map(parse_users)

    def groups(self) -> Result[List[Group], str]:
        """Get a list of auth groups in this team."""
        return get_resource(self.links["groups"].href).map(parse_groups)


def parse_teams(teams_json: Dict[str, Any]) -> List[Team]:
    """Parse JSON into a list of Teams."""
    if "_embedded" not in teams_json or "teamList" not in teams_json["_embedded"]:
        return []
    return parse_obj_as(List[Team], teams_json["_embedded"]["teamList"])
