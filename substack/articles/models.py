from django.db import models
import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length = 150)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add = True)
    thumbnail = models.ImageField(default='logo.png', blank = True)
    #author

    def __str__(self):
        return self.title
    
    def article_snippet(self):
        wordsList = self.body.split(' ')[0:30]
        return ' '.join(wordsList) + '...'

    def MonthDayYear(self):
        months= {'01':'Jan', '02':'Feb', '03':'Mar', 
                 '04':'Apr', '05':'May', '06':'Jun', 
                 '07':'Jul', '08':'Aug', '09':'Sep', 
                 '10':'Oct', '11':'Nov', '12':'Dec'}
        mdy = self.date.strftime("%m-%d-%y").split('-')
        return f"{months[mdy[0]]} {mdy[1]}"
        

#class for articles by a user linking foreign keys

