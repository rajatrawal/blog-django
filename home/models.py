from django.db import models

# Create your models here.
class Contact(models.Model):
    c_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.EmailField(default="")
    phone=models.CharField(max_length=13,default="")
    decs=models.TextField(max_length=500,default="")
    time_stamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name


