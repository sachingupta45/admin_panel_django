from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=self.normalize_email(email), username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ('Batsman', 'Batsman'),
        ('Bowler', 'Bowler'),
        ('All-Rounder', 'All-Rounder'),
        ('Wicket-Keeper', 'Wicket-Keeper'),
    ]
    EXPERIENCE_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    ACTIVITY_CHOICES = [
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
        ('Athlete', 'Athlete'),
    ]
    TRAINING_GOAL_CHOICES = [
        ('Fat Loss', 'Fat Loss'),
        ('Muscle Gain', 'Muscle Gain'),
        ('Maintain', 'Maintain'),
        ('Performance', 'Performance'),
    ]
    DIET_TYPE_CHOICES = [
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),
        ('Vegan', 'Vegan'),
        ('Keto', 'Keto'),
        ('Paleo', 'Paleo'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('blocked', 'Blocked'),
    ]

    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    height_cm = models.DecimalField(max_digits=5, decimal_places=2)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    dob = models.DateField()
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, null=True, blank=True)
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, null=True, blank=True)
    training_goal = models.CharField(max_length=20, choices=TRAINING_GOAL_CHOICES)
    diet_type = models.CharField(max_length=20, choices=DIET_TYPE_CHOICES, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    food_allergies = models.TextField(null=True, blank=True)
    food_preferences = models.TextField(null=True, blank=True)
    meals_per_day = models.IntegerField(null=True, blank=True)
    sleep_hours = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    practice_type = models.JSONField(null=True, blank=True)
    injuries = models.TextField(null=True, blank=True)
    profile_photo = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return f"{self.username} ({self.role})"

    @property
    def is_staff(self):
        return True

    @property
    def is_superuser(self):
        return True

    @property
    def is_active(self):
        return self.status == 'active'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
