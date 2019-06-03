from django.contrib import admin
from .models import Detail, Comment, Hashtag

# Register your models here.
admin.site.register(Detail)
admin.site.register(Comment)
admin.site.register(Hashtag)