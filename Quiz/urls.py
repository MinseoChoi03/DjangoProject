from django.urls import path
from . import views

app_name = 'Quiz'

urlpatterns=[
    path('', views.main, name='main'),
    path('makeQuestion/', views.Questions, name='questions'),
    path('solveQuiz/', views.Quiz, name='solve'),

    path('Questions/', views.insertQuiz, name='insertQuiz'),
    path('answers/', views.insertAnswer, name='insertAnswer')
]