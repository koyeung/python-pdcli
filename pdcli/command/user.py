"""Implement pd user command."""
import json

from ..api.user import get_user, ls_user


def user(user_id: str = None) -> str:
    """Get user.

    :param user_id: user id.
        "me" for current user (not applicable if account-level access token is used).
        List all user if unspecified.

    :return: user dictionaries in json
    """
    result = get_user(user_id=user_id) if user_id else ls_user()

    return json.dumps(result)
