from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    subject = models.CharField(max_length=100,)

class Tags(models.Model):
    image= models.ImageField(upload_to='media/images', default="")
    heading= models.CharField(max_length=100, blank=True, null=True)
    desc= models.CharField(max_length=100, blank=True,null=True)

    class Meta:
     verbose_name='Tag'
     verbose_name_plural='Tags'
     
    

    def __str__(self):
        return self.heading