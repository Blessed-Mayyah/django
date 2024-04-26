from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Sitter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    next_of_kin = models.CharField(max_length=100)
    nin = models.CharField(max_length=20)
    recommender_name = models.CharField(max_length=100)
    religion = models.CharField(max_length=50, blank=True, null=True)
    education_level = models.CharField(max_length=100)
    sitter_number = models.CharField(max_length=20, unique=True)
    contacts = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Baby(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)
    time_of_arrival = models.DateTimeField()
    parents_names = models.CharField(max_length=200)
    fee_in_ugx = models.DecimalField(max_digits=10, decimal_places=2)
    period_of_stay = models.CharField(max_length=100)
    baby_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.baby} by {self.sitter} - {self.payment_date}"

class ProcurementItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    resold_to_babies = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
