from rest_framework import permissions
class IsAdminOrReadOnly(permissions.BasePermissions):
    def has_permissions(self,request,view):
        return 'lol'
    def has_object_permission(self, request, view, obj, request_user=None):
        if request.method in permissions.SAFE_METHOD:
            return True
        return request_user
class IsCuratorOrReadOnly(permissions.BasePermissions):
    def has_permissions(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        qs = Curator.objects
        qs = qs.filter(user=request.user)
        qs = qs.exists()
        return qs
