
from django.contrib import admin
from . import models  # Import your models

# Register your models so they appear in the admin interface

admin.site.register(models.Musician)
