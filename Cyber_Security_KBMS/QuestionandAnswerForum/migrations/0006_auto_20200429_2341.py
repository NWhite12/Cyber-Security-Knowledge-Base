# Generated by Django 2.2.6 on 2020-04-30 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionandAnswerForum', '0005_questionrelpy_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionrelpy',
            name='reply_rank',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
    ]