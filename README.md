##Database final project

Additionally, it provides functionality for comment replies, a profanity filter with a modqueue for review restricted to admin access, and a billing feature.
Generation of elements is modable using plaintext dictionaries.

Command summary follows:

Delete all database tables:
"python3 manage.py flush"

Generate new tables
"python3 manage.py gen_everything"

Add more comments
"python3 manage.py gen_comments"

Access mod queue
"python3 manage.py comments_queue"

Calculate billing to companies
"python3 manage.py bill_companies"

Dictionaries available in
"./dictionaries"

Start server
"python3 manage.py runserver"

By default, this web runs at
"localhost:8000/articles"

