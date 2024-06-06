from django.db import models


class Department(models.Model):
    """department table"""
    name = models.CharField(max_length=32)


class Employee(models.Model):
    """employee table"""
    name = models.CharField(verbose_name='Name', max_length=32)
    password = models.CharField(verbose_name='Password', max_length=32)
    department = models.ForeignKey(to=Department, to_field='id', on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='Age')
    account = models.DecimalField(verbose_name='Account', max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(verbose_name='CreateTime')
    gender_choices = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(verbose_name='Gender', max_length=1, choices=gender_choices)
