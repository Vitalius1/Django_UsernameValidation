from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def validate(self, postData):
        size = len(postData)
        if size>= 8 and size<= 16:
            if not self.filter(name = postData):
                self.create(name = postData)
                msg = {'succes':'The user name you entered (' + postData + ') is valid. Thank You!'}
            else:
                msg = {'error':'The username you entered ('+ postData +') already exists. Try another one!'}
        else:
            msg = {'error':'Username is not valid. Provide a name between 8 and 16 characters.'}
        return msg
    def show_all(self):
        return self.all()
    def remove(self, id):
        self.filter(id = id).delete()

class User(models.Model):
    name = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

# Create your models here.
