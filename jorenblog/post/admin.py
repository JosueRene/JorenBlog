from django.contrib import admin

# Register your models here.
from .models import Type, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'created_by', 'created_at')

admin.site.register(Type)
admin.site.register(Post, PostAdmin)
