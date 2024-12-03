from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)   
    identifier = models.PositiveBigIntegerField(null=True)    
   
    REQUIRED_FIELDS=['name', 'email',]

    def has_role_or_group(self, roles_or_groups):
        # Verificar roles
        user_roles = self.roles.values_list('name', flat=True)
        if any(role in user_roles for role in roles_or_groups):
            return True

        # Verificar grupos
        user_groups = self.groups.values_list('name', flat=True)
        if any(group in user_groups for group in roles_or_groups):
            return True

        return False