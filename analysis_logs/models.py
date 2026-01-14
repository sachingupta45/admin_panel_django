from django.db import models
from users.models import User

class MealAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal_analyses')
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_unit = models.CharField(max_length=20, null=True, blank=True)
    meal_time = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)
    ai_response = models.TextField()
    item_name = models.CharField(max_length=100, null=True, blank=True)
    calories = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    protein_g = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    carbs_g = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fats_g = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fiber_g = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    sugar_g = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    meal_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Meal Analyses"
        db_table = 'meal_analysis'

    def __str__(self):
        return f"{self.item_name} - {self.user.username}"

class RequiredDietLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diet_logs')
    diet_date = models.DateField(auto_now_add=True)
    calories = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    carbs_g = models.DecimalField(max_digits=10, decimal_places=2)
    fats_g = models.DecimalField(max_digits=10, decimal_places=2)
    fiber_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugar_g = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'diet_date')
        db_table = 'required_diet_logs'

    def __str__(self):
        return f"Diet Log {self.diet_date} - {self.user.username}"

class WaterIntakeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='water_logs')
    water_ml = models.IntegerField()
    logged_at = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)
    water_time = models.DateTimeField(null=True, blank=True)
    bottle_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.water_ml}ml - {self.user.username}"
