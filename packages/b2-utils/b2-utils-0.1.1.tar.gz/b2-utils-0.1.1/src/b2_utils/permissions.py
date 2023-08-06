from rest_framework import exceptions, permissions


class IsSafeMethods(permissions.BasePermission):
    def has_permission(self, request, _):
        return request.method in permissions.SAFE_METHODS


class IsAnonymous(permissions.BasePermission):
    def has_permission(self, request, _):
        return request.user.is_anonymous


class IsValidVersion(permissions.BasePermission):
    def has_permission(self, request, _):
        if not request.version:
            raise exceptions.NotAcceptable()

        return True
