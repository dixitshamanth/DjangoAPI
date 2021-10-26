# Generated by Django 3.2.7 on 2021-09-30 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_course_courseinstructor_instructor_instructorappointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseinstructor',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='courseinstructor',
            name='instructor_id',
        ),
        migrations.RemoveField(
            model_name='instructorappointment',
            name='instructor_id',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='CourseInstructor',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.DeleteModel(
            name='InstructorAppointment',
        ),
    ]
