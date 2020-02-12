from django.shortcuts import render
from django.shortcuts import redirect
from .forms import QueryForm
from . import models
import string

# Create your views here.
def query(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        #token question
        if form.is_valid():
            context={}
            query = form.cleaned_data['query']
            tokens = query.split(' ')
            entries = []
            for asset in tokens:
                try:
                    entry = models.KnowledgeBaseEntry.objects.get(topic=asset)
                    entries.append(entry)
                except:
                    entry = None
            context['results'] = entries      
            return render(request, 'CSKnowledgeBase/queryResults.html',context)
    else:
    #give form
        form = QueryForm()
    return render(request, "CSKnowledgeBase/query.html", {"form": form})