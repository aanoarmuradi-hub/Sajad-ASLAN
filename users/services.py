from django.core.exceptions import PermissionDenied
from .models import User

def require_role(current_user, allowed_roles):
    if current_user.role not in allowed_roles:
        raise PermissionDenied("You don't have permission")


def add_user(current_user, username, password, role):

    require_role(current_user, ["admin"])

    if not username:
        raise ValueError("Enter username")

    if not password:
        raise ValueError("Enter password")

    if role not in ["admin", "user"]:
        raise ValueError("Invalid role")

    user = User.objects.create_user(
        username=username,
        password=password,
        role=role
    )

    return user