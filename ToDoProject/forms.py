from models import ToDoItem
from django import forms
from django.forms import ModelForm


class ToDoItemForm(ModelForm):

    delete = forms.BooleanField(required=False)

    class Meta:
        model = ToDoItem
        fields = ['item_text']


