from django.db import models
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
   COLORS={
      (1, 'black'),
      (2, 'yellow'),
      (3, 'red')
   }
   heading=models.CharField(max_length=127,null=True,blank=True)
   desc=models.TextField(help_text='Bura blog desc hissedir...!')
   created_at=models.DateTimeField(auto_now_add=True)
   color=models.IntegerField(choices=COLORS)
   is_active=models.BooleanField(default=True)
   slug=models.CharField(max_length=255,null=True, blank=True)

   # relation
   category=models.ForeignKey('Category', on_delete=models.CASCADE)
   blog_tags = models.ManyToManyField('Tag')
   author=models.ForeignKey('Author', on_delete=models.CASCADE)
   
class Category(models.Model):
   name=models.CharField(max_length=127,)
   text=models.TextField(max_length=127)
   updated_at=models.DateTimeField(auto_now=True)
  
# cemleme
   class Meta:
      verbose_name='Blog'
      verbose_name_plural='Blogs'
      # en son elave edilen datani 1 cini gosterir
      ordering = ('-created_at')

class Tag(models.Model):
   title = models.CharField(max_length=127, null=True,blank=True)


def __str__(self):
    return self.heading
   
# def get_absolute_url(self):
#       return reverse('blog:blog', args=[self.slug])




# info
class Author(models.Model):
   name=models.CharField(max_length=257,blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)

class Meta:
      verbose_name='Muellif'
      verbose_name_plural='Muellifler'
      ordering = ('-created_at')




def __str__(self):
    return self.name
