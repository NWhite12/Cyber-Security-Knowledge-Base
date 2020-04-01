from django.contrib import admin
from .models import *
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_title', 'date_posted', 'posted_by', 'expertise_required')

class QuestionRelpyAdmin(admin.ModelAdmin):
    list_display = ('reply_header', 'submitted_by', 'question', 'expertise_required')

class QuestionExpertiseAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'expertise_id')

class QuestionTopicAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'topic_id')

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionRelpy, QuestionRelpyAdmin)
admin.site.register(QuestionExpertise, QuestionExpertiseAdmin)
admin.site.register(QuestionTopic, QuestionTopicAdmin)

