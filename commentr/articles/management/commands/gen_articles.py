from django.core.management.base import BaseCommand, CommandError
from articles.models import Article

from django.utils import timezone
import random
import time

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.localtime


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)


class Command(BaseCommand):
    def handle(self, *args, **options):
        companies = open("dictionaries/companies").readlines()
        fnames = open("dictionaries/fnames").readlines()
        lnames = open("dictionaries/lnames").readlines()
        topics = open("dictionaries/topics").readlines()
        #titles = ["thi", "tha"]#open("dictionaries/titles").readlines()
        titles = open("dictionaries/titles").readlines()
        random.shuffle(titles)
        titles = titles[1:100]

        for title in titles:
            a = Article()
            a.customer = random.choice(companies).rstrip()
            a.author = random.choice(fnames).rstrip() + " " + random.choice(lnames).rstrip()
            a.topic = random.choice(topics).rstrip()
            a.pub_date = timezone.now()
            a.title = title.rstrip()

            a.save()

        print(str(len(titles)) + " articles added")


