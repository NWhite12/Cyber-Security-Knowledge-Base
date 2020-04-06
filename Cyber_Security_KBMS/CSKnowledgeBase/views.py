import json
import string

from CSKnowledgeBase.models import Knowledge
from QuestionandAnswerForum.models import Question
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from .forms import QueryForm


# Create your views here.
def query(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    else:
        if request.method == "POST":
            form = QueryForm(request.POST)
            #token question
            if form.is_valid():
                context={}
                stopWordsAndPunct = set(stopwords.words('english') + list(string.punctuation))
                query = form.cleaned_data['query']
                tokens = word_tokenize(query)
                filteredTokens = [word for word in tokens if not word in stopWordsAndPunct]
                knowledgeEntries = Knowledge.objects.none()
                questionEntries = Question.objects.none()
                for item in filteredTokens:
                    knowledgeEntries = (knowledgeEntries | Knowledge.objects.filter(name__icontains=item)| Knowledge.objects.filter(content__icontains=item))
                    questionEntries = (questionEntries | Question.objects.filter(question_title__icontains=item) | Question.objects.filter(content__icontains=item))

                    print(knowledgeEntries)

                context['knowledgeResults'] = knowledgeEntries.distinct()
                context['questionResults'] = questionEntries.distinct()
                return render(request, 'CSKnowledgeBase/queryResults.html', context)
        else:
        #give form
            form = QueryForm()
            return render(request, "CSKnowledgeBase/query.html", {"form": form})

def viewknowledge(request, knowledge_id, slug):

    #if not logged in make them login
    if not request.user.is_authenticated:
       return redirect('http://127.0.0.1:8000/login')
    else:
        context = {}

        #find particular question with specified id and slug
        knowledge = Knowledge.objects.get(id=knowledge_id, slug=slug)
        # assuming obj is a model instance
        # seralize question into json format
        # json.loads() -> parses JSON string
        knowledge_json = json.loads(serializers.serialize('json', [ knowledge ]))[0]['fields']

        #Assigns those dictionary entries values
        knowledge_json['update_date'] = knowledge.update_date
        knowledge_json['kid'] = knowledge.id
        knowledge_json['knowledge_text'] = knowledge.content

        #Assign context dictionary to question_json
        context['knowledge'] = knowledge_json
        return render(request, 'view-knowledge.html', context)

