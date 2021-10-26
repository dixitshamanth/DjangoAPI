# Generated by Django 3.2.7 on 2021-09-30 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
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
