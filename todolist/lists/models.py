from random import choice

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, DateInput
from django.urls import reverse

class Lists(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    class MPTTMeta:
      order_insertion_by = ['created_at']

    def __str__(self):
        return self.name

class Items(models.Model):
    STATUS = (
        ('True', 'Completed'),
        ('False', 'Continue')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS)
    description = models.CharField(blank=True, max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=False)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

class ListForm(ModelForm):
    class Meta:
        model = Lists
        fields = ['name','slug']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'name'}),
            'slug': TextInput(attrs={'class': 'input', 'placeholder': 'slug'}),
        }
        def get_absolute_url(self):
            return reverse('addlist', kwargs={'slug': self.slug})


class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ['name','description','deadline','slug']
        widgets = {
            'deadline': DateInput(attrs={'class': 'DateInput', 'placeholder': 'enter deadline'}),
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'name'}),
            'slug': TextInput(attrs={'class': 'input', 'placeholder': 'slug'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder':'description'})
        }
        def get_absolute_url(self):
            return reverse('additem', kwargs={'slug': self.slug})