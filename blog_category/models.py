from django.db import models

# Create your models here.
class PostCategory(models.Model):

    title= models.CharField(max_length=50)
    name = models.CharField(max_length=50)


    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories" 

    def __str__(self):
        return self.title