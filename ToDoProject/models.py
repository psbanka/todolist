from django.db import models
from django.contrib.auth.models import User
from django import forms


class ToDoItem(models.Model):
    item_text = models.CharField(max_length = 100)
    user = models.ForeignKey(User)

    def __unicode__(self):
       return self.item_text

class ToDoListForm(forms.Form):
    add_item = forms.CharField(max_length=100)
    user = models.ForeignKey(User)
    deleteItem = forms.BooleanField(required=False)

    def __unicode__(self):
        return self.add_item, self.deleteItem

