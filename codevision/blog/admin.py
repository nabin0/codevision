from django.contrib import admin
from .models import Post, PostComments
# Register your models here.
admin.site.register((Post, PostComments))