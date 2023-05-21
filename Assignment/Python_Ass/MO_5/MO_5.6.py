"""
---> Write program to create a new Post object in database
-Django Models
        A Django model is the built-in feature that Django uses to create tables, 
    their fields, and various constraints. In short, Django Models is the SQL of Database
    one uses with Django. SQL (Structured Query Language) is complex and involves a 
    lot of different queries for creating, deleting, updating or any other stuff related 
    to database. Django models simplify the tasks and organize tables into models.
    Generally, each model maps to a single database table. 

Each model is a Python class that subclasses django.db.models.Model.

Each attribute of the model represents a database field.
 
 With all of this, Django gives you an automatically-generated database-access API; 
see Making queries.
Example – 
 
"""
from django.db import models
 
# Create your models here.
class TopsModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
