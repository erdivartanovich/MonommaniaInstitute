from django.db import models
from django.utils import timezone

class Post(models.Model):
	"""Model untuk Post"""
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	tanggal = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.tanggal = timezone.now()
		self.save

	def __str__(self):
		return self.title


# Create your models here.
