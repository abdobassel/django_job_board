from django.db import models

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
    #category
    experience = models.IntegerField(default=1)
    #apply job 
    #post job





    def __str__(self):
        return str(self.title)