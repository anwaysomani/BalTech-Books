from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from organizations.models import *
from .constants import *

import uuid

# Employee auth
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email or not password:
            raise ValueError('User must have a username and password')
        user = self.model(
            email=CustomUserManager.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password,**kwargs)

        user.is_admin = True
        user.is_staff = True
        user.save()

        return user


# Employee Privileges
class employee_privilege_table(models.Model):
    privilege_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=45)
    permissions = models.CharField(max_length=40)
    max_allowed_members = models.IntegerField()
    current_members = models.IntegerField

    class Meta:
        verbose_name = "Employee's Privilege"
        verbose_name_plural = "Employee's Privileges"

# Contstants: userType, city, state, country
class employee_table(AbstractBaseUser):
    employee_id = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobileNumber = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    pincode = models.IntegerField(null=True)
    state = models.CharField(max_length=35, null=True)
    country = models.CharField(max_length=50, null=True)
    organization_id = models.ForeignKey(organization_table, null=True, blank=True)
    privilege_id = models.ForeignKey(employee_privilege_table, null=True, blank=True)
    joining_date = models.DateField(auto_now=True, null=True, blank=True)
    last_login = models.DateTimeField(null=True)
    termination_date = models.DateField(null=True, blank=True)
    is_user = models.NullBooleanField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    api_token = models.UUIDField(default=uuid.uuid4, editable=False)
    token_created_date = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['employee_id', 'first_name', 'mobileNumber']

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def api_token_reset(self):
        self.api_token = models.UUIDField(default=uuid.uuid4, editable=False)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


