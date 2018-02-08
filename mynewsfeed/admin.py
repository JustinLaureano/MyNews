from django.contrib import admin
from .models import RedditPost, CourierPost, NYTimesPost, GuardianPost

admin.site.register(RedditPost)
admin.site.register(CourierPost)
admin.site.register(NYTimesPost)
admin.site.register(GuardianPost)
