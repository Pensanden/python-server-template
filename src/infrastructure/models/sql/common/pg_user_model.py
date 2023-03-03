from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from .base_pg_model import BasePgModel


class PgUserModel(BasePgModel, AbstractUser):
    __domain_class__ = None

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=
        'The groups this user belongs to. A user will get all permissions '
        'granted to each of their groups.'
        ,
        related_name="rasa_user_set",
        related_query_name="rasa_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="rasa_user_set",
        related_query_name="rasa_user",
    )

    class Meta:
        verbose_name_plural = "Users"
        db_table = 'users'
