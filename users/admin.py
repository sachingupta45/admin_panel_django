from django.contrib import admin
from django.contrib.auth.models import Group, User as AuthUser
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'status', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role', 'status', 'training_goal')
    list_per_page = 10

    def has_add_permission(self, request):
        return False

# Unregister Group and User models from Authentication section
try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(AuthUser)
except admin.sites.NotRegistered:
    pass
