from django.core.management.base import BaseCommand, CommandError
from articles.models import Comment, User, Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Comments flagged for review by moderator:")
        print("Enter \"q\" at any time to quit")
        print()
        print("Please enter admin credentials")
        user = input("email: ")
        admins = User.objects.filter(admin=True, email=user)
        if len(admins) == 0 :
            print("Invalid email")
            quit()
        else:
            pw = input("password: ")
            access = False
            for admin in admins:
                if admin.password == pw:
                    access = True
        if access == False:
            print("Invalid password")
            quit()


        print()


        comments = Comment.objects.filter(flag=True)

        for comment in comments:
            ans = ''
            done = False
            while done == False:
                print(str(comment.user) + "  [" + comment.pub_date.strftime("%Y-%m-%d %H:%M") + "]")
                print(comment.content)
                print("Posted on article: " + str(comment.article.title))
                ans = input("Approve comment? (y/n) ")
                if(ans == 'q'):
                    quit()
                elif(ans == 'y'):
                    comment.flag = False
                    print("Comment approved")
                    done = True
                elif(ans == 'n'):
                    comment.content = "[Comment removed by moderator]"
                    comment.flag = False
                    print("Comment permenantly deleted")
                    done = True
                else:
                    print("Invalid input")
                comment.save()
            print()
        print("Queue is empty")


