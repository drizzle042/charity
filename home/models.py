from django.db import models

# Create your models here.
class Latest_new(models.Model):
	"""docstring for Latest_news"""
	title = models.CharField(max_length = 120)
	slug = models.SlugField()
	images = models.ImageField()
	story = models.TextField()
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	def snippet(self):
		return self.story [0:500] + '...' 


class topstorie(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	thumb = models.ImageField()
	story = models.TextField()
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	def snippet(self):
		return self.story [:400] + "..."




