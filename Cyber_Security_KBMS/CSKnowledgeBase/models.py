from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category_title = models.CharField(max_length=50)

    def __str__(self):
        return self.category_title
    

class KnowledgeBaseEntry(models.Model):
    topic = models.CharField(max_length=50)
    category = models.OneToOneField(Category, on_delete = models.PROTECT)
    content = models.TextField()
    date_last_modified = models.DateTimeField()
    last_modified_by  = models.ForeignKey(User, on_delete = models.PROTECT)
    def save(self):
        #update the time on save and modifed
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(KnowledgeBaseEntry, self).save()
    
    def __str__(self):
        return self.topic

class Keywords(models.Model):
    keyword = models.CharField(max_length=50)

    def __str__(self):
        return self.keyword

class Expertise(models.Model):
    expertise_title = models.CharField(max_length=50)
    def __str__(self):
        return self.keyword

class EntrySubEntry(models.Model):
    entry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='entry')
    subentry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='subentry')

class AssetEntryCountermeasureEntry(models.Model):
    asset_entry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='protected_asset')
    countermeasure_entry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='countermeasure')

class ThreatEntryVulnerabilityEntry(models.Model):
    threat_entry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='exploiting_threat')
    vulnerability_entry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='utlized_vulnerability')

class AssetEntryThreatEntry(models.Model):
    asset_entry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='threatened_asset')
    threat_entry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='threating_entry')

class AssetEntryVulnerabilityEntry(models.Model):
    asset_entry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='affected_asset')
    vulnerability_entry_id = models.ForeignKey(KnowledgeBaseEntry, on_delete=models.PROTECT, related_name='present_vulnerability')
