from rest_framework.permissions import BasePermission
from choices import Role


class IsAdminOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        is_allowed = True

        if request.method in ('POST', 'PATCH', 'PUT', 'DELETE'):
            is_allowed = (
                request.user.role == Role.ADMIN or request.user.is_superuser
            )

        return is_allowed


class IsAdminOrSuperuserOrManager(BasePermission):
    def has_permission(self, request, view):
        is_allowed = True

        if request.method in ('POST', 'PATCH', 'PUT', 'DELETE'):
            is_allowed = (
                request.user.role == Role.ADMIN or
                request.user.role == Role.MANAGER or
                request.user.is_superuser
            )
        return is_allowed
