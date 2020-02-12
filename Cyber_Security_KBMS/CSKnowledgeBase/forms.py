from django import forms
from . import models

class QueryForm(forms.Form):
    query = forms.CharField(label='Query', max_length = 100)