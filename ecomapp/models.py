from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class WomenCategory(models.Model):
   women = models.CharField(max_length=50,unique=True)
   def __str__(self):
      return self.women

class MenCategory(models.Model):
   men = models.CharField(max_length=50,unique=True)
   def __str__(self):
      return self.men

class GirlsCategory(models.Model):
   kids = models.CharField(max_length=50,unique=True)
   def __str__(self):
      return self.kids

class BoysCategory(models.Model):
   kids = models.CharField(max_length=50,unique=True) 
   def __str__(self):
      return self.kids

class Size(models.Model):
   size = models.CharField(max_length=50,null=True)
   def __str__(self):
      return self.size
         
class KidsAge(models.Model):
   age = models.CharField(max_length=50,unique=True,null=True)
   def __str__(self):
      return self.age

def user_directory_path(instance,filename):  
    if isinstance(instance,WomenFashion):
      x = "women"
    elif isinstance(instance,MenFashion):
      x = "men"
    elif isinstance(instance,GirlsFashion):
      x = "girls"
    elif isinstance(instance,BoysFashion):
      x = "boys"
    else:
      pass
    return '{0}/{1}/{2}'.format(x,instance.category,filename)

#The base class for all 4 databases

class iambase(models.Model):
  seller = models.CharField(max_length=50)
  description = models.CharField(max_length=60)
  price = models.IntegerField()
  card_image = models.ImageField(upload_to=user_directory_path) 
  upload_date = models.DateTimeField(auto_now=True)
  size = models.ManyToManyField(Size)
  class Meta:
    abstract = True

class WomenFashion(iambase):
   category = models.ForeignKey(WomenCategory, on_delete=models.CASCADE)

class MenFashion(iambase):
    category = models.ForeignKey(MenCategory, on_delete=models.CASCADE)

class GirlsFashion(iambase):
    category = models.ForeignKey(GirlsCategory, on_delete=models.CASCADE)
    age = models.ManyToManyField(KidsAge)

class BoysFashion(iambase):
    category = models.ForeignKey(BoysCategory, on_delete=models.CASCADE)
    age = models.ManyToManyField(KidsAge)
    

