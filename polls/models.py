from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(verbose_name='Question Text', max_length=100)
    pub_date = models.DateTimeField(verbose_name='Date Published', auto_now=True)
