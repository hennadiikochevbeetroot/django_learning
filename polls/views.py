from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    latest_questions = Question.objects.order_by('-pub_date')
    five_latest = latest_questions[:5]
    return render(request, 'polls/index.html', {'questions': five_latest})


def question(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/question.html', {'question': question})


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'Result for question {question_id}')


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'Voted for question {question_id}')


def message(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Message!')
