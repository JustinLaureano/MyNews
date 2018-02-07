from django.shortcuts import render
from .models import RedditPost


def newsfeed(request):
    reddit_all = RedditPost.objects.all()
    return render(request, 'mynewsfeed/news.html', {'reddit_all': reddit_all})
