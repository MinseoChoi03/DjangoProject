from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from Quiz.models import Quiz_questions, Quiz_answer


def main(request):
    return render(request, 'Quiz/Main.html')


def Questions(request):
    return render(request, 'Quiz/makeQuestion.html')


def Quiz(request):
    return render(request, 'Quiz/solveQuiz.html')


def insertQuiz(request):
    question = request.POST['question']
    answer = request.POST['answer']
    hint = request.POST['hint']

    qs = Quiz_questions(quiz_question=question, quiz_answer=answer, quiz_hint=hint)
    qs.save()

    return HttpResponseRedirect(reverse('Quiz:main'))


def insertAnswer(request):
    answer = request.POST['answer']

    qs = Quiz_answer(answer=answer)
    qs.save()

    return HttpResponseRedirect(reverse('Quiz:Check'))


def Quiz(request):
    qs = Quiz_questions.objects.all()
    context = {'Quiz_list': qs}
    return render(request, 'Quiz/solveQuiz.html', context)