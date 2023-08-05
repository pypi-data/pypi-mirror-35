# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Class(models.Model):
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    department = models.CharField(max_length=4, blank=True, null=True)
    code = models.CharField(max_length=4, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    credits = models.TextField(blank=True, null=True)  # This field type is a guess.
    attributes = models.TextField(blank=True, null=True)
    level = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    all_sections = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'class'


class Department(models.Model):
    abbr = models.CharField(max_length=4, blank=True, null=True)
    title = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'department'


class Instructor(models.Model):
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'instructor'


class Location(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    building = models.TextField(blank=True, null=True)  # This field type is a guess.
    room = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Section(models.Model):
    section_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    uid = models.TextField(blank=True, null=True)  # This field type is a guess.
    section = models.TextField(blank=True, null=True)  # This field type is a guess.
    department = models.CharField(max_length=4, blank=True, null=True)
    code = models.CharField(max_length=4, blank=True, null=True)
    semester = models.CharField(max_length=6, blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)  # This field type is a guess.
    campus = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    method = models.TextField(blank=True, null=True)  # This field type is a guess.
    catalog_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    bookstore_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    syllabus = models.TextField(blank=True, null=True)  # This field type is a guess.
    days = models.CharField(max_length=7, blank=True, null=True)
    location = models.SmallIntegerField(blank=True, null=True)
    starttime = models.TimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    instructor = models.TextField(blank=True, null=True)  # This field type is a guess.
    finalexam = models.DateTimeField(db_column='finalExam', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'section'


class Semester(models.Model):
    id = models.CharField(max_length=6, blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    registrationstart = models.TextField(db_column='registrationStart', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    registrationend = models.DateField(db_column='registrationEnd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'semester'
