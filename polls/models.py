from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(verbose_name='Date Published', auto_now=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name='Choice Text', max_length=100)
    votes = models.IntegerField(verbose_name='Amount of Votes', default=0)
