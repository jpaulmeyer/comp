# Create your models here.
from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


#https://www.newswhip.com/2013/12/article-length/#OmwfEoL0L3SUP43q.97
class Article(Content):
    text = models.TextField(max_length=10000)
    
    ''' Not sure if this will work because of the self variable?
    def show(self):
    	print "{}, {}, by {}, on {}".format(self.title, self.subtitle, self.contributors, self.pub_date)
    '''

class Image(Content):
    path = models.ImageField(max_length=500)

    def info():
    	print self.path


class Contributor(models.Model):
    pass