import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    customer = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length = 50)
    topic = models.CharField(max_length = 50)
    pub_date = models.DateTimeField('date published')
    #last_updated = models.DateTimeField('last updated')

    def __str__(self):
        headline = self.title + "<br /> By " + self.author + "<br />"
        body = "Published by " + self.customer + " in " + self.topic + " on "
        tail = self.pub_date.strftime('%Y-%m-%d %H:%M') + "<br />"

        return headline + body + tail

class User(models.Model):
    email = models.CharField(max_length=50)
    hash_code = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #comment_type = models.IntegerField()
    content = models.CharField(max_length=140)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
    flag = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        headline = str(self.user) + " [" + self.pub_date.strftime("%Y-%m-%d %H:%M") + "]: " + "<br /> &emsp;"
        if(self.flag == False):
            body = self.content
        else:
            body = "[Comment flagged for review by moderator]\n"
        tail = "<br />"
        return headline + body + tail

class Filter_Words(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


