from django.db import models
from django.utils.text import slugify
# Create your models here.


class Question(models.Model):
    qid=models.AutoField(primary_key=True)
    question_title=models.CharField(max_length=100)
    question_text=models.TextField(max_length=50000)
    date_posted=models.DateTimeField(auto_now_add=True)
    posted_by=models.TextField(max_length=20)
    #Slug = provides url for question to be referenced later
    slug=models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question_title)
        super(Question,self).save(*args,**kwargs)
