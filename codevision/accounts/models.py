from django.db import models

# Create your models here.

class UserDetail(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.IntegerField()
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)

    def __str__(self) -> str:
        return "The Username is : "+ self.username
