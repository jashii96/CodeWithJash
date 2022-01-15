import builtins
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50 ,null = False)
    slug = models.CharField(max_length=50, null = False, unique=True)
    description = models.CharField(max_length=300)
    price = models.IntegerField(null= False)
    discount = models.IntegerField(null= False, default=0)
    active =models.BooleanField(default=False)
    thumbnail =models.ImageField(upload_to ='files/thumbnails')
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to='files/resource')
    length =models.IntegerField(null=False)

    def __str__(self):
        return self.name

class classProperty(models.Model):
    description = models.CharField(max_length= 500)
    course = models.ForeignKey(Course, null= False, on_delete= models.CASCADE)

    class Meta:
        abstract = True


class Tag(classProperty):
    pass

class Prerequisite(classProperty):
    pass

class Learning(classProperty):
    pass