from django.db import models


class Quiz_questions(models.Model):
    quiz_question = models.CharField(max_length=500)
    quiz_answer = models.CharField(max_length=100)
    quiz_hint = models.CharField(max_length=500)

    def __str__(self):
        return self.quiz_question


class Quiz_answer(models.Model):
    answer = models.IntegerField(max_length=100)

    def __str__(self):
        return self.answer