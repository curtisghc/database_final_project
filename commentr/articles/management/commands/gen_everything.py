from django.core.management.base import BaseCommand, CommandError
import subprocess

class Command(BaseCommand):
    def handle(self, *args, **options):
        subprocess.call("python3 manage.py gen_articles", shell = True)
        subprocess.call("python3 manage.py gen_users", shell = True)
        subprocess.call("python3 manage.py gen_comment_filter", shell = True)
        subprocess.call("python3 manage.py gen_comments", shell = True)
