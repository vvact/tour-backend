import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email) if email else ''
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    # Public identifier – UUID (secure, unguessable)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        help_text=_('Public identifier for the user')
    )

    # Extra fields – only what we need
    phone_number = PhoneNumberField(
        _('phone number'),
        blank=True,
        null=True,
        help_text=_('Contact phone number')
    )
    profile_picture = models.ImageField(
        _('profile picture'),
        upload_to='profile_pics/',
        blank=True,
        null=True
    )
    bio = models.TextField(
        _('bio'),
        max_length=500,
        blank=True,
        help_text=_('Tell us a bit about yourself')
    )

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.get_full_name() or self.username

    @property
    def full_name(self):
        return self.get_full_name()