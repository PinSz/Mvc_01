from __future__ import unicode_literals
from django.db import models
from functools import partial


# Create your models here.
class Exam(models.Model):
	name = models.CharField(max_length=150, default='')
	description = models.TextField(null=True, blank=True)
	published = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Quiz(models.Model):
	exam = models.ForeignKey(Exam)
	name = models.CharField(max_length=200, default='')
	image = models.FileField(upload_to='upload', null=True, blank=True)

	def __str__(self):
		return self.name
  
class Choice(models.Model):
	quiz = models.ForeignKey(Quiz)
	name = models.CharField(max_length=200, default='')
	corrected = models.BooleanField(default=False)

	def __str__(self):
		return self.name
# .....................................................
class Department(models.Model):
	DeptCode = models.CharField(max_length=2, blank=False)
	DeptName = models.CharField(max_length=20)

class Employee(models.Model):
	EmpNo = models.CharField(max_length=3, default='',blank=False)
	FName = models.CharField(max_length=20, blank=False)
	LName = models.CharField(max_length=20, blank=False)
	SEX_CHOICES = [('M','Male'), ('F', 'Female')]
	Sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
	# GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    # Sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
	Salary = models.IntegerField(default=0)
	StartDate = models.DateField(blank=True)
	DeptCode = models.ForeignKey(Department,on_delete=models.CASCADE)
	published = models.BooleanField(default=True)
