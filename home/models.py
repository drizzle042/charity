from django.db import models

# Create your models here.

# Email Modelform to map to database for receiving email from users
class Email(models.Model):
	email = models.EmailField()

	def __str__(self):
		return self.email

# The profiles database Modelform to map to database
class Profile(models.Model):
	profile_cover_photo = models.ImageField(default = 'profile-photo.png', blank = True)
	profile_photo = models.ImageField(default = 'profile-photo.png', blank = True)
	first_name = models.CharField(max_length = 14)
	last_name = models.CharField(max_length = 14)
	slug = models.SlugField()
	about_snippet = models.CharField(max_length = 60)
	followers = models.IntegerField(default = 1, blank = True)
	events = models.IntegerField(default = 0, blank = True)
	donations = models.IntegerField(default = 0, blank = True)
	event_photos = models.ImageField(blank = True)
	address_field = models.CharField(max_length = 40, blank = True)
	mobile_contact = models.PositiveBigIntegerField(blank = True)
	email = models.EmailField(blank = True)
	facebook_contact = models.CharField(max_length = 20, blank = True)
	twitter_contact = models.CharField(max_length = 20, blank = True)
	about = models.TextField()
	date = models.DateField()
