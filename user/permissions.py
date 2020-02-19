from rest_framework.permissions import BasePermission


class IsAdminOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        is_allowed = True

        if request.method in ('POST', 'PATCH', 'PUT', 'DELETE'):
            is_allowed = (
                request.user.role == 'ADMIN' or request.user.is_superuser
            )

        return is_allowed
