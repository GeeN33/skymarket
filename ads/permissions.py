from rest_framework import permissions


class CreatePermission(permissions.BasePermission):
    message = 'User not author!'

    def has_permission(self, request, view):
        r = request.data['author']
        u = request.user

        if r == u.id:
            return True
        return False


class UpdateDeletePermission(permissions.BasePermission):
    message = 'User not author or admin!'

    def has_permission(self, request, view):
        r = request.data['author']
        u = request.user

        if u.role == 'admin':
            return True
        elif r == u.id:
            return True
        else:
            return False


