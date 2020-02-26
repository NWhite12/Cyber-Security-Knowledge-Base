from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Knowledge)
admin.site.register(Expertise)
admin.site.register(Topic)
admin.site.register(EntrySubEntry)
admin.site.register(UserExpertise)
admin.site.register(KnowledgeTopic)
admin.site.register(KnowledgeRelationLookUp)

