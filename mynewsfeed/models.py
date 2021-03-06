from django.db import models


class RedditPost(models.Model):

    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500, blank=True)
    comments = models.CharField(max_length=500, blank=True)
    subreddit = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class CourierPost(models.Model):

    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class NYTimesPost(models.Model):

    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class GuardianPost(models.Model):

    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500, blank=True)
    trailText = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title
