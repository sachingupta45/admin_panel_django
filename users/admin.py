from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'status', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role', 'status', 'training_goal')

    def has_add_permission(self, request):
        return False
