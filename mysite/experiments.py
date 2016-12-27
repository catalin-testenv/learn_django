import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

if __name__ == '__main__' and __package__ is None:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('BASE_DIR ', BASE_DIR)
    sys.path.append(BASE_DIR)


import django
django.setup()

# ===========================================================

from django.db import connection, connections, reset_queries

from polls.models import Question, Choice

reset_queries()

print(Question.objects.all())

print(connection.queries)
