from django.db import models

# Create your models here.
class Contact(models.Model):
    # sno=models.AutoField()
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    # phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self) -> str:
        return self.name
class DR(models.Model):
    id=models.AutoField(primary_key=True)
    name1=models.CharField(max_length=122)
    email1=models.CharField(max_length=122)
    phone1=models.CharField(max_length=122)
    gender=models.CharField(max_length=122,default="")
    age=models.CharField(max_length=122,default="")

    right=models.ImageField(null=True ,blank=True,upload_to="shop/images")
    left=models.ImageField(null=True ,blank=True,upload_to="shop/images")
    rprediict=models.CharField(max_length=122,default="")
    lpredict=models.CharField(max_length=122,default="")
    def __str__(self) -> str:
        return self.name1