from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    #authors = models.ManyToManyField(Author)
    #publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    content = models.TextField()
    tel = models.TextField()

    def __unicode__(self):
        return self.title

class Totalspots(models.Model):
	name = models.CharField(max_length=50)
	cities = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	telephone = models.CharField(max_length=15)
	longitude = models.FloatField()
	latitude = models.FloatField()
	content = models.TextField()

	def __unicode__(self):
		return self.name

class Cities(models.Model):
	cities = models.CharField(max_length=10)
	city = models.CharField(max_length=10)

	def __unicode__(self):
		return self.cities