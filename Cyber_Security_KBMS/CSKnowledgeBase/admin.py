from django.contrib import admin
from .models import *
# Register your models here.

class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'insert_date', 'update_date')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EntrySubEntryAdmin(admin.ModelAdmin):
    list_display = ('parent_id', 'child_id')

class KnowledgeRelationLookUpAdmin(admin.ModelAdmin):
    list_display = ('asset_entry_id', 'countermeasure_entry_id', 'threat_entry_id', 'vulnerability_entry_id', 'policy_entry_id')

class KnowledgeTopicAdmin(admin.ModelAdmin):
    list_display = ('knowledge_id', 'topic_id')

class UserExpertiseAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'expertise_id')


admin.site.register(Knowledge, KnowledgeAdmin)
admin.site.register(Expertise, ExpertiseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(EntrySubEntry, EntrySubEntryAdmin)
admin.site.register(UserExpertise)
admin.site.register(KnowledgeTopic, KnowledgeTopicAdmin)
admin.site.register(KnowledgeRelationLookUp, KnowledgeRelationLookUpAdmin)

