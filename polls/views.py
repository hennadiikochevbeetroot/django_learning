from django.http import HttpRequest, HttpResponse

from .models import Question


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    latest_questions = Question.objects.order_by('-pub_date')
    five_latest = latest_questions[:5]
    latest_questions_text = ''
    for question in five_latest:
        latest_questions_text += question.question_text
        latest_questions_text += '\n'

    return HttpResponse(f'Latest questions:\n {latest_questions_text}')


def question(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'Question {question_id}')


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'Result for question {question_id}')


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'Voted for question {question_id}')


def message(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Message!')
