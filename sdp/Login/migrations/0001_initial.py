# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('street_no', models.CharField(blank=True, max_length=100)),
                ('house_no', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=100)),
                ('credit', models.FloatField()),
                ('type', models.CharField(choices=[('Theory', 'Theory'), ('Lab', 'Lab')], default='Theory', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.FloatField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Course')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_id', models.CharField(help_text='You can use small letters [a-z] and digits [0-9] only', max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mail_id', models.EmailField(max_length=100)),
                ('dob', models.DateField(help_text='YYYY-MM-DD')),
                ('year_of_enrollment', models.PositiveIntegerField(help_text='Use the following format: <YYYY>')),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='')),
                ('is_alumni', models.BooleanField(default=False)),
                ('industry', models.CharField(blank=True, max_length=100)),
                ('headline', models.CharField(blank=True, max_length=200)),
                ('summary', models.CharField(blank=True, max_length=200)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.Address')),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.College')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.Department')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.School')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Student'),
        ),
        migrations.AddField(
            model_name='department',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.University'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.Department'),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('country', 'city', 'area', 'street_no', 'house_no')]),
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together=set([('student', 'course')]),
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together=set([('name', 'university')]),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('course_code', 'department')]),
        ),
    ]
