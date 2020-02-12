from django.conf.urls import url, include
from CSKnowledgeBase import views
from CSKnowledgeBase.views import *
from django.urls import path

urlpatterns = [
#specify path to homepage
#r - raw string, ^ means begin with, $ - ends with, begins and ends with nothing means its the homepage
#view.index view that should be shown when homepage url is specified

    path('submit-query',views.query),
    
]
