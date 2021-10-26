from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Instructor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    classCode = models.CharField(max_length=200)
    courseTitle = models.CharField(max_length=100)

    def __str__(self):
        return self.classCode


class InstructorAppointment(models.Model):
    id = models.IntegerField(primary_key=True)
    examplefield = models.CharField(max_length=200)
    active = models.IntegerField()
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.examplefield


class CourseInstructor(models.Model):
    id = models.IntegerField(primary_key=True)
    sampleField = models.CharField(max_length=200)
    course_instructor_id = models.ForeignKey(
        InstructorAppointment, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.sampleField
