from rest_framework import serializers
from .models import Instructor, Course, CourseInstructor, InstructorAppointment


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email']


class InstructorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorAppointment
        fields = ['id', 'examplefield',
                  'home_department_id', 'active', 'instructor_id']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'classCode', 'courseTitle']


class CourseInstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInstructor
        fields = ['id', 'sampleField', 'instructor_id', 'course_id']
