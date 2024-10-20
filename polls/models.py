import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(verbose_name='Date Published', auto_now=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self) -> bool:
        now = timezone.now()
        yesterday = now - datetime.timedelta(days=1)
        return yesterday <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name='Choice Text', max_length=100)
    votes = models.IntegerField(verbose_name='Amount of Votes', default=0)

    def __str__(self):
        return self.choice_text
