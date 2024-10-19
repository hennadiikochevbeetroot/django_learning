from django.db.models import F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse

from .models import Choice, Question


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
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {"question": question, "error_message": "You didn't select a choice."}
        return render(request, "polls/question.html", context)

    selected_choice.votes = F("votes") + 1
    selected_choice.save()
    return redirect(reverse("polls:results", args=(question.id,)))


def message(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Message!')
