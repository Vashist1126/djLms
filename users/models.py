from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Override these ManyToMany fields to provide unique reverse accessors
    # and avoid clashes with the built-in auth.User related_names.
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users_custom_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users_custom_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    ROLE_CHOICES=[
        ('ADMIN','admin'),
        ('LEARNER','learner'),
        ('TRAINER','trainer'),
    ]

    role= models.CharField(max_length=20,choices=ROLE_CHOICES,default='LEARNER')

    def __str__(self):
        return f"{self.username} ({self.role})"
