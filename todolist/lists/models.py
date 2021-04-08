from django.db import models

# Create your models here.
class Lists(models.Model):

    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
      order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Items(models.Model):
    STATUS = (
        ('True', 'Completed'),
        ('False', 'Continue')
    )
    list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS)
    description = models.CharField(blank=True, max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name