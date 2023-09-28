from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    
    def create_user(self, login, password, **extra_fields):
        groups = extra_fields.pop('groups', [])
        permissions = extra_fields.pop('user_permissions', [])
        user = self.model(
            login=login,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        user.groups.set(groups)
        user.user_permissions.set(permissions)
        user.save()
        return user
    
    def create_superuser(self, login, password):
        user = self.model(
            login=login,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(
        max_length=100,
        unique=True,
    )
    name = models.CharField(
        max_length=100
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_superuser = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = "login"

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.login
