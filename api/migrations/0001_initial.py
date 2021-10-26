# Generated by Django 3.2.7 on 2021-09-30 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classCode', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InstructorAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=200)),
                ('active', models.IntegerField()),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='CourseInstructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sampleField', models.CharField(max_length=200)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instructor')),
            ],
        ),
    ]
