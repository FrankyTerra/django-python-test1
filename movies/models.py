from datetime import datetime
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Genre(models.Model):
	genre_name = models.CharField(max_length=100)

	def __str__(self):
		return self.genre_name

class Country(models.Model):
	country_name = models.CharField(max_length=100)

	def __str__(self):
		return self.country_name

class Film(models.Model):
	film_name = models.CharField(max_length=200)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	year_of_issue = models.DateField()
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	producer = models.CharField(max_length=200)
	pub_date = models.DateField('date published', default=datetime.now)
	cast = models.TextField()

	def __str__(self):
		return self.film_name

class Comment(MPTTModel):
	film = models.ForeignKey(Film, null=True, on_delete=models.CASCADE)
	parent = TreeForeignKey('self', blank=True, null=True, related_name='children', db_index=True)
	author = models.CharField(max_length=100)
	text = models.TextField()
	pub_date = models.DateTimeField('date published', default=datetime.now)

	class MPTTMeta:
		order_insertion_by = ['pub_date']

	def __str__(self):
		return self.author