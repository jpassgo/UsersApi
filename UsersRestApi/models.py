from django.db import models


class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    age = models.IntegerField()

    def __unicode__(self):
        return self.name + ' - ' + self.email + ' - ' + self.age + ' - ' + self.id
