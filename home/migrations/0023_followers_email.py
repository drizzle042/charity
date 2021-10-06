# Generated by Django 3.2.6 on 2021-10-02 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_email_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers_email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile', models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
    ]
