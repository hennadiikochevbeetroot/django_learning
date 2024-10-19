import datetime
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


# Create your tests here.


class TestQuestion(TestCase):
    def test_was_published_recently_now(self):
        q = Question(question_text='Question text', pub_date=timezone.now())
        self.assertIs(q.was_published_recently(), True)

    def test_was_not_published_recently_future(self):
        q = Question(question_text='Question text', pub_date=timezone.now() + datetime.timedelta(days=7))
        self.assertIs(q.was_published_recently(), False)


class TestViews(TestCase):
    def test_empty_db(self):
        questions_url = reverse('polls:index')
        response = self.client.get(questions_url)
        self.assertIs(response.status_code, HTTPStatus.OK.value)
        self.assertContains(response, 'No Questions found!')
        self.assertEqual(list(response.context['questions']), [])

    def test_two_questions(self):
        question1 = Question.objects.create(question_text='Q1', pub_date=timezone.now())
        question2 = Question.objects.create(question_text='Q2', pub_date=timezone.now())
        questions_url = reverse('polls:index')
        response = self.client.get(questions_url)
        self.assertIs(response.status_code, HTTPStatus.OK.value)
        self.assertNotContains(response, 'No Questions found!')
        self.assertEqual(list(response.context['questions']), [question2, question1])

    def test_question_view(self):
        question = Question.objects.create(question_text='Q1', pub_date=timezone.now())
        choice1 = Choice.objects.create(question=question, choice_text='C1', votes=0)
        choice2 = Choice.objects.create(question=question, choice_text='C2', votes=0)

        # Test detail view
        question_url = reverse('polls:question', args=(question.id,))
        response = self.client.get(question_url)
        self.assertContains(response, question.question_text)
        self.assertContains(response, choice1.choice_text)
        self.assertContains(response, choice2.choice_text)
        self.assertContains(response, 'Vote for choice')

        # Test voting
        # FIXME: fix tests for voting
        # votes_url = reverse('polls:vote', args=(question.id,))
        # selected_choice_id = choice1.id
        # self.client.post(
        #     votes_url,
        #     data=urlencode({'choice': selected_choice_id}),
        #     content_type="application/x-www-form-urlencoded",
        # )
        # self.assertEqual(choice1.votes, 1)
