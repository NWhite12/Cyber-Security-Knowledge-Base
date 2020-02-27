from django.http import HttpResponse
from django.shortcuts import render, redirect
from QuestionandAnswerForum.models import *
from django.core import serializers

import json
import markdown2
import bleach

def index(request):
    #show what homepage should look like
    # goes to home.html
    return render(request, 'home.html', {})

def askquestion(request):
     if request.method == 'POST':
        try:
            q_title = request.POST.get('title')
            q_question = request.POST.get('question')
            q_posted_by = request.POST.get('posted_by')
            #Save question query in q
            q = Question(question_title=q_title, content=q_question, posted_by=q_posted_by)
            #save question to database
            q.save()

            #Question completed correct go to viewquestion function, sending questions id and slug

            return redirect(viewquestion, q.id, q.slug)
        except Exception as e:
            # Question not entered correctly
            return render(request, 'ask-question.html', { 'error': 'Something is wrong with the form!' })
     else:
        return render(request, 'ask-question.html', {})

def seeQuestion (request):
    #Dictionary
    context={}
    #modifying dictionary to add question entry
    context['questions']=Question.objects.all()
    return render(request, 'seeQuestions.html',context)


def viewquestion(request, question_id, slug):
    context = {}

    #find particular question with specified id and slug
    question = Question.objects.get(id=question_id, slug=slug)



    # assuming obj is a model instance
    # seralize question into json format
    # json.loads() -> parses JSON string
    question_json = json.loads(serializers.serialize('json', [ question ]))[0]['fields']

    #Assigns those dictionary entries values
    question_json['date_posted'] = question.date_posted
    question_json['qid'] = question.id
    question_json['question_text'] = question.content

    #Assign context dictionary to question_json
    context['question'] = question_json

    return render(request, 'view-question.html', context)
