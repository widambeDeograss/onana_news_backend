from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    GENDER = (
        ("M", "MALE"),
        ("F", "FEMALE")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER, null=True, blank=True, max_length=6)
    profile = models.ImageField(upload_to="uploads/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=12, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', "phone_number"]

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'

