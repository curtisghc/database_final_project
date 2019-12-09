from django.core.management.base import BaseCommand, CommandError
from articles.models import Article, Comment

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Billing handled at a flat rate of 10 cents per comment")

        companies = Article.objects.values('customer').distinct().values('customer')

        for company in companies:
            company = company['customer']
            count = Comment.objects.filter(article__customer=company).count()
            print(company + " owes $" + str(float(count / 10)) + " for " + str(count) + " comments")
