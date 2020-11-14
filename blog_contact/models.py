from django.db import models

# Create your models here.
class Contact(models.Model):

    fullname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    subject = models.CharField(max_length=50)
    text = models.TextField()
    # date = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField()


    def __str__(self):
        return self.subject