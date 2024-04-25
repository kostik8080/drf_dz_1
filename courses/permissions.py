from rest_framework.permissions import BasePermission, SAFE_METHODS


class ModeratorPermission(BasePermission):
    """Проверяет, что пользователь является модератором."""
    def has_permission(self, request, view):
        if request.user.is_staff and request.user.groups.filter(name="moderator").exists():
            return True
        return False


class IsUser(BasePermission):
    """Проверяет, что пользователь является владельцем."""

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
