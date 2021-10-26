from django.contrib import admin
from .models import Instructor, InstructorAppointment, CourseInstructor, Course

# Register your models here.
admin.site.register(Instructor)
admin.site.register(InstructorAppointment)
admin.site.register(CourseInstructor)
admin.site.register(Course)
