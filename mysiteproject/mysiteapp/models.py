from django.db import models
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
# Create your models here.
    def __str__(self):
        return self.name
class person(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='pics1')
    desc1=models.TextField()

    def __str__(self):
        return self.name1
