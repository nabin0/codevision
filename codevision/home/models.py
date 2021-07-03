from django.db import models

# Models Here

class Contact(models.Model):
    sn = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    phone = models.IntegerField()
    msg = models.TextField(max_length=5000)
    contactedDate = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return "Contacted By: " + self.name

