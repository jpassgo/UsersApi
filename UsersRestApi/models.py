from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    age = models.IntegerField()
    id = models.AutoField()
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_added=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.name + ' - ' + self.email + ' - ' + self.age + ' - ' + self.id 
