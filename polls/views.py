from django.db.models import F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from django.views.generic import DetailView, ListView
from django.utils import timezone

from .models import Choice, Question


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        # select *
        # from questions
        # where pub_date <= now()
        # order by pub_date desc;
        latest_five_questions = Question.objects \
             .filter(pub_date__lte=timezone.now()) \
             .order_by('-pub_date')[:5]

        return latest_five_questions


class QuestionView(DetailView):
    model = Question
    template_name = 'polls/question.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'


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
