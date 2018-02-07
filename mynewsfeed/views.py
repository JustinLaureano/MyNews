from django.shortcuts import render


def newsfeed(request):
    return render(request, 'mynewsfeed/news.html', {})
