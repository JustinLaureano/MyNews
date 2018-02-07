from django.shortcuts import render
from .models import RedditPost, CourierPost


def newsfeed(request):
    reddit_all = RedditPost.objects.all()
    courier_all = CourierPost.objects.all()
    content = {'reddit_all': reddit_all, 'courier_all': courier_all}
    return render(request, 'mynewsfeed/news.html', content)