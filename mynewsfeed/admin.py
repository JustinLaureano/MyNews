from django.contrib import admin
from .models import RedditPost, CourierPost

admin.site.register(RedditPost)
admin.site.register(CourierPost)