from django.db import models

# Create your models here.


class Movie(models.Model):
    mvname=models.CharField('mv_name',max_length=100)
    mvreviews = models.CharField('mv_reviews', max_length=100)
    mvcategory = models.CharField('mv_category', max_length=100)
    active = models.CharField('active', max_length=100,default='Y')


class Actor(models.Model):
    aname = models.CharField('mv_name', max_length=100)
    aexprc = models.IntegerField('mv_name')
    active = models.CharField('active', max_length=100, default='Y')


class MovieActor(models.Model):
    movie = models.ForeignKey('Movie',unique=False,on_delete=models.CASCADE,null=False)
    actor = models.ForeignKey('Actor',unique=False,on_delete=models.CASCADE,null=False)


