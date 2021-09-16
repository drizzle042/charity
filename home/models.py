from django.db import models

# Create your models here.

# Email form to map to database
class Email(models.Model):
	email = models.EmailField()

	def __str__(self):
		return self.email