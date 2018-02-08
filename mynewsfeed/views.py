from django.shortcuts import render
from .models import RedditPost, CourierPost, NYTimesPost, GuardianPost


def newsfeed(request):
    reddit_all = RedditPost.objects.all()
    courier_all = CourierPost.objects.all()
    ny_times = NYTimesPost.objects.all()
    guardian = GuardianPost.objects.all()

    content = {'reddit_all': reddit_all, 'courier_all': courier_all,
               'ny_times': ny_times, "guardian": guardian}

    return render(request, 'mynewsfeed/news.html', content)
