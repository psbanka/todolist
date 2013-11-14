from django.db import models
from django.contrib.auth.models import User


class ToDoItem(models.Model):
    item_text = models.CharField(max_length = 100)
    user = models.ForeignKey(User)

    def __unicode__(self):
       return self.item_text

