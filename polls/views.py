from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello world')


def question(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'Question {question_id}')


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'Result for question {question_id}')


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f'Voted for question {question_id}')


def message(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Message!')
