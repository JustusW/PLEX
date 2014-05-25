from django.contrib import admin
from django.db import models

class Memplex(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=300)

    def __str__(self):              # __unicode__ on Python 2
        return "%s - %s" % (self.title.encode('utf-8'), self.text.encode('utf-8'))

class Path(models.Model):
    type = models.CharField(max_length=30)
    weight = models.IntegerField()

    memplex = models.ManyToManyField(Memplex)

    def __str__(self):              # __unicode__ on Python 2
        return self.type + '@' + self.weight.__str__()


admin.site.register(Memplex)
admin.site.register(Path)