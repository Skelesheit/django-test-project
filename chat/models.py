from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


# Create your models here.

class Chat(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'
        ARCHIVED = 'archived', 'Archived'

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    description = models.TextField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(blank=False, null=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Измените related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class ChatParticipant(models.Model):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        USER = 'user', 'User'

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.USER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.chat} - {self.profile} - {self.role}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # ладно я не знаю на самом деле
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.chat) + str(self.profile) + str(self.content)
