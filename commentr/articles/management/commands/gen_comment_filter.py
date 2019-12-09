from django.core.management.base import BaseCommand, CommandError
from articles.models import Filter_Words


class Command(BaseCommand):
    def handle(self, *args, **options):
        dictionary = open("dictionaries/profanity").readlines()

        for word in dictionary:
            f = Filter_Words()
            f.word = word.rstrip()
            f.save()
            #print(f)

        print(str(len(dictionary)) + " profane words added to dictionary")


