from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Knowledge(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.TextField()
    last_modified_by  = models.ForeignKey(User, on_delete = models.PROTECT)
    insert_date = models.DateTimeField()
    update_date = models.DateTimeField()
    
        #Slug = provides url for question to be referenced later
    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        #update the time on save and modifed
        if not self.id:
            self.insert_date = timezone.now()
        self.update_date = timezone.now()
        return super(Knowledge, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Expertise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class EntrySubEntry(models.Model):
    parent_id = models.ForeignKey(Knowledge, on_delete=models.PROTECT, related_name = "parent")
    child_id = models.ForeignKey(Knowledge, on_delete=models.PROTECT, related_name = "child")
    class Meta:
        unique_together = ["parent_id", "child_id"]

class KnowledgeRelationLookUp (models.Model):
    asset_entry_id = models.ForeignKey(Knowledge, on_delete=models.PROTECT, related_name = "asset")
    countermeasure_entry_id = models.ForeignKey(Knowledge, on_delete=models.PROTECT,  related_name = "countermeasure")
    threat_entry_id = models.ForeignKey(Knowledge, on_delete=models.PROTECT, related_name = "threat")
    vulnerability_entry_id = models.ForeignKey(Knowledge, on_delete=models.PROTECT, related_name = "vulnerability")
    policy_entry_id =  models.ForeignKey(Knowledge, on_delete=models.PROTECT, related_name = "policy")

    class Meta:
        unique_together = ["asset_entry_id", "countermeasure_entry_id", "threat_entry_id", "vulnerability_entry_id", "policy_entry_id"]

class KnowledgeTopic(models.Model):
    knowledge_id = models.ForeignKey(Knowledge, on_delete=models.PROTECT)
    topic_id = models.ForeignKey(Topic, on_delete=models.PROTECT)

    class Meta:
        unique_together = ["knowledge_id", "topic_id"]

class UserExpertise(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    expertise_id = models.ForeignKey(Expertise, on_delete = models.PROTECT)

    class Meta:
        unique_together = ["user_id", "expertise_id"]
