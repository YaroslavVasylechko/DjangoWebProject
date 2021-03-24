from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anouncement = models.CharField('Anouncement', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'all news'