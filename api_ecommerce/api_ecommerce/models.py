from django.contrib.auth.models import AbstractUser, AbstractBaseUser
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'administrator'),
        (2, 'normal')
    )