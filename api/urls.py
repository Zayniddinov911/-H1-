from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addQuiz),
    path('true/', views.getTrueAnswers),
    path('questions/', views.getQuestions),
    path('user/', views.getUser),
    path('add_user/', views.addUser),

]
