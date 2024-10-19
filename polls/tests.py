import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


# Create your tests here.


class TestQuestion(TestCase):
    def test_was_published_recently_now(self):
        q = Question(question_text='Question text', pub_date=timezone.now())
        self.assertIs(q.was_published_recently(), True)

    def test_was_not_published_recently_future(self):
        q = Question(question_text='Question text', pub_date=timezone.now() + datetime.timedelta(days=7))
        self.assertIs(q.was_published_recently(), False)
