# Generated by Django 3.2.6 on 2021-09-26 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_rename_advert_images_advert_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topstory_images',
            new_name='Topstory_image',
        ),
    ]
