# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 03:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_exam_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeptCode', models.CharField(max_length=2)),
                ('DeptName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpNo', models.CharField(default='', max_length=3)),
                ('FName', models.CharField(max_length=20)),
                ('LName', models.CharField(max_length=20)),
                ('Sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Salary', models.IntegerField(default=0)),
                ('StartDate', models.DateField()),
                ('DeptCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Department')),
            ],
        ),
    ]
