from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name = 'director')
    actors = models.ManyToManyField(Person, through='Role')
    year = models.IntegerField()

class Role(models.Model):
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)
    role = models.CharField(max_length=128)
