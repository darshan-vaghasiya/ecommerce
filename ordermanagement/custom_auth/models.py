from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators


class User(AbstractUser):
    username = models.CharField(
        'username',
        max_length=30,
        unique=True,
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                'Enter a valid username. This value may contain only letters, numbers ' 'and @/./+/-/_ characters.',
            ),
        ],
        error_messages={
            'unique': 'A user with that username already exists.',
        },
    )
    email = models.EmailField('email address')
    otp = models.CharField(max_length=4, default='0000')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
