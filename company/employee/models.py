from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField()
    ename = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img',blank=True,null=True)

    def __str__(self):
        return self.empid