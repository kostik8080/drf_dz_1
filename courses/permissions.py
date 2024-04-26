from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsModer(BasePermission):
    """Проверяет, что пользователь является модератором."""
    def has_permission(self, request, view):
        if request.user.groups.filter(name="moderator").exists():
            return True
        return False


class IsOwner (BasePermission):
    """Проверяет, что пользователь является владельцем."""

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
