from django.core.management.base import BaseCommand, CommandError
from articles.models import User
import hashlib
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        emails = open("dictionaries/emails").readlines()
        random.shuffle(emails)
        emails = emails[1:100]
        country = ["USA", "Algeria", "Austraila"]

        for email in emails:
            email = email.rstrip()
            u = User()
            u.hash_code = hashlib.md5(bytes(email, "ascii")).hexdigest
            u.password = "password"
            u.country = random.choice(country)
            u.email = email

            u.save()

        u = User()
        u.email = "admin@commentr.com"
        u.hash_code = hashlib.md5(bytes(u.email, "ascii")).hexdigest
        u.password = "password"
        u.country = random.choice("USA")
        u.admin = True
        u.save()

        print(str(len(emails) + 1) + " users added")


