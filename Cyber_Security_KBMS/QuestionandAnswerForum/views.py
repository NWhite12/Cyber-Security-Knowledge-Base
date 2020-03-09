from django.http import HttpResponse
from django.shortcuts import render, redirect
from QuestionandAnswerForum.models import *
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
import json
import markdown2
import bleach
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
    return render(request, 'home.html', {})

def askquestion(request):

     if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
     if request.method == 'POST':
        try:
            q_title = request.POST.get('title')
            q_question = request.POST.get('question')
            q_posted_by = request.user

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
    if not request.user.is_authenticated:
       return HttpResponseRedirect('login')
    #Dictionary
    else:
        context={}
        #modifying dictionary to add question entry
        context['questions']=Question.objects.all()
        return render(request, 'seeQuestions.html',context)


def viewquestion(request, question_id, slug):

    #if not logged in make them login
    if not request.user.is_authenticated:
       return redirect('http://127.0.0.1:8000/login')
    else:
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
        question_json['posted_by']=question.posted_by.username

        #Assign context dictionary to question_json
        context['question'] = question_json



        #Display answers to questions if there are any
        try:
            context['reply'] =  QuestionRelpy.objects.filter(question_id=question_id)

        except ObjectDoesNotExist:
            print("No Answers to this question")

        #Display form for users to input answers
        if request.method == 'POST':

             a_header = request.POST.get("answer_title")
             a_content = request.POST.get("answer")
             question = Question.objects.get(id=question_id, slug=slug)
             user = request.user

             #save form information into a questionrelpy query
             a = QuestionRelpy( reply_header = a_header, content = a_content,reply_rank=0.5,question = question, submitted_by= user)
             #save to database
             a.save()

             #redirect to question
             return redirect(viewquestion, question.id, question.slug)
        return render(request, 'view-question.html', context)

def user_login(request):
    context={}

    if request.method=="POST":

        username = request.POST.get('username')



        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, "home.html",context)
        else:
            context["error"]="wrong creditabls"
            return render (request, "login.html",context)
    else:
        return render (request, "login.html",context)

def user_logout(request):
    if request.method=="POST":

        logout(request)
        return HttpResponseRedirect('login')

def user_profile(request):
    if not request.user.is_authenticated:
       return redirect('http://127.0.0.1:8000/login')
    else:
       context= {'firstname' : request.user.username}

       #display user questions if there are any
       try:
           context['question'] =  Question.objects.filter(posted_by=request.user)
       except ObjectDoesNotExist:
           print("No questions by user")

    return render(request, "user_profile.html",context)
