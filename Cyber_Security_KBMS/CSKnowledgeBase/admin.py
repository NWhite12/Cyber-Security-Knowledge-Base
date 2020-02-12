from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(KnowledgeBaseEntry)
admin.site.register(Keywords)
admin.site.register(Expertise)
admin.site.register(EntrySubEntry)
admin.site.register(AssetEntryCountermeasureEntry)
admin.site.register(ThreatEntryVulnerabilityEntry)
admin.site.register(AssetEntryThreatEntry)
admin.site.register(AssetEntryVulnerabilityEntry)