from django.contrib import admin
from .models import MealAnalysis, RequiredDietLog, WaterIntakeLog

@admin.register(MealAnalysis)
class MealAnalysisAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'user', 'calories', 'meal_date', 'meal_time')
    search_fields = ('item_name', 'user__username')
    list_filter = ('meal_date',)
    list_per_page = 10

    def has_add_permission(self, request):
        return False

@admin.register(RequiredDietLog)
class RequiredDietLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'diet_date', 'calories', 'protein_g')
    list_filter = ('diet_date',)
    list_per_page = 10
    
    def has_add_permission(self, request):
        return False

@admin.register(WaterIntakeLog)
class WaterIntakeLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'water_ml', 'logged_at')
    list_filter = ('logged_at',)
    list_per_page = 10

    def has_add_permission(self, request):
        return False
