from django.contrib import admin

from chat import models

# Register your models here.

admin.site.register(models.Chat)

admin.site.register(models.CustomUser)

admin.site.register(models.ChatParticipant)

admin.site.register(models.Message)
