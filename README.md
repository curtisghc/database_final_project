## Database final project
Commentr is an app that generates articles, and populates them with comments using python3 and the Django framework

Additionally, it provides functionality for comment replies, a profanity filter with a modqueue for review restricted to admin access, and a billing feature.
Generation of elements is modable using plaintext dictionaries.

Command summary follows:

|Command | Description|
|-|-|
|`python3 manage.py flush`| Delete all database tables |
|`python3 manage.py gen_everything`| Generate new tables |
|`python3 manage.py gen_comments`| Add more comments |
|`python3 manage.py comments_queue`| Access mod queue |
|`python3 manage.py bill_companies`| Calculate billing to companies |
|`python3 manage.py runserver`| Start webserver |

By default, this web app runs at

`localhost:8000/articles`


Dictionaries available in

`./dictionaries`
