from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class GreatKartUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        """ Customise create_user method to add error if email is not set """
        if not email:
            raise ValueError('The given email must be set')

        return super(GreatKartUserManager, self).create_user(username, email, password, **extra_fields)


class GreatKartUser(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(max_length=50)

    # Use email to login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = GreatKartUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
