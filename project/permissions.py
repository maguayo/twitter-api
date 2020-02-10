from django.conf import settings
from rest_framework.permissions import AllowAny


class ActionBasedPermission(AllowAny):
    def has_permission(self, request, view):
        for klass, actions in getattr(view, "action_permissions", {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False