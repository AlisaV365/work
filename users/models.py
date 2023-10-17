from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from goodhabits.models import NULLABLE

class User(AbstractUser):
    username = None
    surname = models.CharField(max_length=35, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    chat_id = models.CharField(max_length=20, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class RootRole(AbstractUser):
    is_root = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='root_roles')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='root_roles')

    class Meta:
        verbose_name = 'Root Role'
        verbose_name_plural = 'Root Roles'
