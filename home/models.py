from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField

# Create your models here.

# Email Modelform to map to database for receiving email from users
class Email(models.Model):
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.email

# The profiles database Model to map to database
class Profile(models.Model):
	profile_cover_photo = models.ImageField(default = 'profile/profile_cover_photos/profile-photo.png', blank = True, upload_to = 'profile/profile_cover_photos/')
	profile_photo = models.ImageField(default = 'profile/profile_photos/profile-photo.png', blank = True, upload_to = 'profile/profile_photos/')
	first_name = models.CharField(max_length = 14)
	last_name = models.CharField(max_length = 14)
	slug = models.SlugField()
	about_snippet = models.CharField(max_length = 120)
	followers = models.IntegerField(default = 1, blank = True)
	events = models.IntegerField(default = 0, blank = True)
	donations = models.IntegerField(default = 0, blank = True)
	address_field = models.CharField(max_length = 40, blank = True)
	mobile_contact = models.PositiveBigIntegerField(blank = True)
	email = models.EmailField(blank = True)
	facebook_contact = models.CharField(max_length = 20, blank = True)
	twitter_contact = models.CharField(max_length = 20, blank = True)
	about = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.slug
	
# Profiles Event_photos database Model to map to database. This inherits from Profile and attaches here using a foreignkey
class Profile_event_photo(models.Model):
	profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
	event_photos = models.ImageField(blank = True, upload_to = 'profile/events_images/', default = 'profile/events_images/photos-gallery icon.png')

	def __str__(self):
		return self.profile.slug

# News database Model to map to database
class Headline(models.Model):
	title = models.CharField(max_length = 40)
	image = models.ImageField(default = 'news-images/photos-gallery icon.png', upload_to = 'news-images/')
	slug = models.SlugField()
	story_snippet = models.CharField(max_length = 160)
	story = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title

#  Flash messages database Model 
class Advert(models.Model):
	title = models.CharField(max_length=120)
	first_message = models.CharField(max_length=250)
	body = models.TextField()
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

# Advert photos 
class Advert_image(models.Model):
	advert = models.ForeignKey(Advert, on_delete=CASCADE)
	photos = models.ImageField(upload_to='news-images/', blank=True)

	def __str__(self):
		return self.advert.slug

# Motivational messages
class Topstory(models.Model):
	title = models.CharField(max_length=120)
	body = models.TextField()
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body [:450]

# Motivational messages photos
class Topstory_image(models.Model):
	story = models.ForeignKey(Topstory, on_delete=CASCADE)
	photos = models.ImageField(upload_to='news-images/', blank=True)

	def __str__(self):
		return self.story.slug