"""Checks for Keycloak token."""
import questionary as q
from jwt import DecodeError
from returns.result import Failure
from returns.result import Result
from returns.result import Success

from dapla_team_cli.auth.services.expiry import has_expired
from dapla_team_cli.auth.services.get_token import get_token
from dapla_team_cli.auth.services.set_token import set_token


def check_token_valid(token: str) -> Result[str, str]:
    """Check if the Keycloak token is valid."""
    try:
        expired = has_expired(token)
    except DecodeError:
        get_new_token = q.confirm("Keycloak token is invalid, do you want to reauthenticate?").ask()
        if not get_new_token:
            return Failure("❌ Keycloak token is invalid")
        set_token(None)
        return check_keycloak()

    if not expired:
        return Success("✅ Keycloak token is set and valid")

    get_new_token = q.confirm("Keycloak token has expired, do you want to reauthenticate?").ask()
    if not get_new_token:
        return Failure("❌ Keycloak token has expired")

    set_token(None)
    return check_keycloak()


def _get_token() -> Result[str, str]:
    """Return token or fail if it is not set."""
    token = get_token()
    if token:
        return Success(token)

    get_new_token = q.confirm("Keycloak token is not set, do you want to authenticate now?").ask()
    if not get_new_token:
        return Failure("❌ Keycloak token not set")

    set_token(None)
    return _get_token()


def check_keycloak() -> Result[str, str]:
    """Check if a keycloak token is set."""
    return _get_token().bind(check_token_valid)
