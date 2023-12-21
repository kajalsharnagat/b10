from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomBookManager(models.Manager):
    def get_active_objects(self):
        return self.filter(isdeleted=False)

    def get_inactive_objects(self):
        return self.filter(isdeleted=True)


class Book(models.Model):
    PUBLICATION_CHOICE = [
        ('pb1', 'Publication 1'),
        ('pb2', 'Publication 2'),
        ('pb3', 'Publication 3'),
        ('pb4', 'Publication 4'),

    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isdeleted = models.BooleanField(default=False)
    price = models.IntegerField()
    objects = CustomBookManager()
    publication_name = models.CharField(max_length=3, choices=PUBLICATION_CHOICE, null=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL) # null


    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"



class FileUpload(models.Model):
    name = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "file_upload"
