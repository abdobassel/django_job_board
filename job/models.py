from django.db import models
from django.utils.text import slugify

# Create your models here.
class Job(models.Model):
    job_choices = [('Fulltime','Fulltime'),
                    ('Parttime','Parttime'),
    ]
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50,choices=job_choices,default='')
    description = models.TextField(max_length=3000,null=True,blank=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to='jobs/')
    slug = models.SlugField(null=True,blank=True)
    #apply job 
    #post job





    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
   
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return str(self.name)



