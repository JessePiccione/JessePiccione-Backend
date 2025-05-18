from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group, User
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        adminGroup = Group.objects.get(name='Admin')
        return user in adminGroup.user_set.all()
        