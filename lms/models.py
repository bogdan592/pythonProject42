from django.db.models import(Model,CharField,ForeignKey,CASCADE)
from django.db import models
from django.utils import timezone
# Create your models here.
class Curator(Model):
    first_name = CharField(max_length=20)
    def __str__(self):
        return "курат. "+self.first_name

class Direction(Model):
    name = CharField(max_length=20)
    curator = ForeignKey(Curator,on_delete=CASCADE,related_name='direction')
    def __str__(self):
        return "напр. "+self.name

class Group(models.Model):
    number = models.CharField(max_length=20)
    deviz = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    direction = models.ForeignKey(Direction,
                                  on_delete=models.CASCADE,
                                  related_name='group')
class Student(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    otchesvo = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    group = ForeignKey(Group,on_delete=CASCADE,related_name='student')