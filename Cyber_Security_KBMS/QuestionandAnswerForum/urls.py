from django.conf.urls import url, include
from QuestionandAnswerForum import views
from QuestionandAnswerForum.views import *
from django.urls import path

urlpatterns = [
#specify path to homepage
#r - raw string, ^ means begin with, $ - ends with, begins and ends with nothing means its the homepage
#view.index view that should be shown when homepage url is specified

    path('',views.index),
    path('ask-question', askquestion,name='askquestion'),
    path('see-questions', seeQuestion),
    path('question/<int:question_id>/<slug:slug>', viewquestion)
]
