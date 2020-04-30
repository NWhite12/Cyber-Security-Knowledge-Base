from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete = models.PROTECT)
    expertise_required = models.BooleanField(default = False)
    #Slug = provides url for question to be referenced later
    slug = models.SlugField(max_length=40)
    anonymous = models.BooleanField(default = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question_title)
        super(Question,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.question_title)



class QuestionRelpy(models.Model):
    id = models.AutoField(primary_key = True)
    reply_header = models.CharField(max_length=120)
    content = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete = models.PROTECT)
    reply_rank = models.IntegerField( default=0)
    question = models.ForeignKey(Question, on_delete = models.PROTECT)
    expertise_required = models.BooleanField(default = False)
    anonymous = models.BooleanField(default = True)
    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.reply_header)
        super(QuestionRelpy,self).save(*args,**kwargs)
    def __str__(self):
        return str(self.reply_header)

class QuestionExpertise(models.Model):
    question_id = models.ForeignKey(Question, on_delete = models.PROTECT)
    expertise_id = models.ForeignKey('CSKnowledgeBase.Expertise', on_delete = models.PROTECT)
    class Meta:
        unique_together = ["question_id", "expertise_id"]



class QuestionTopic(models.Model):
    question_id = models.ForeignKey(Question, on_delete = models.PROTECT)
    topic_id = models.ForeignKey('CSKnowledgeBase.Topic', on_delete = models.PROTECT)
