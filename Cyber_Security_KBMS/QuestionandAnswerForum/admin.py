from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionRelpy)
admin.site.register(QuestionExpertise)
admin.site.register(QuestionTopic)

