# Generated by Django 3.2.6 on 2021-09-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_headline_story_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='story_snippet',
            field=models.CharField(max_length=160),
        ),
    ]
