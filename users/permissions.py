from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission: Users can edit only their own profile.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read permissions (GET, HEAD, OPTIONS) for everyone
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Write permissions are only allowed to the owner
        return obj.id == request.user.id  # Ensure the user is the owner
