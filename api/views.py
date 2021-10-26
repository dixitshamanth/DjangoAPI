from .serializers import InstructorSerializer, InstructorAppointmentSerializer, CourseInstructorSerializer, CourseSerializer
from rest_framework import status
from .models import CourseInstructor, Instructor, InstructorAppointment, Course
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@api_view(["GET"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome to the app!"}
    return JsonResponse(content)


@api_view(["GET"])
@csrf_exempt
# PROTECTS THE ROUTE WITH AUTHENTICATION
@permission_classes([IsAuthenticated])
def get_courses(request):  # FUNCTION TO HANDLE API CALL TO THE ROUTE /api/getcourses
    payload = json.loads(request.body)
    emailKey = payload["email"]  # API Request content: E-mai search key
    instructorKey = Instructor.objects.filter(email=emailKey)

    # print(instructorKey)

    instructorAppointments = InstructorAppointment.objects.filter(
        instructor_id__in=instructorKey, active=1).values("id")  # RETRIEVING INSTRUCTOR IDs with the matching e-mail and appointment being active

    appointmentIds = []
    for i in instructorAppointments:
        appointmentIds.append(i["id"])

    # print(instructorAppointments)
    # print(appointmentIds)

    courseInstructors = CourseInstructor.objects.filter(
        course_instructor_id__in=appointmentIds).values("course_id")  # Mapping INSTRUCTOR APPOINTMENTS table records TO COURSE INSTRUCTOR table

    courseIds = []
    for c in courseInstructors:
        courseIds.append(c["course_id"])

    # print(courseInstructors)
    # print(courseIds)

    # Getting the corresponding list of COURSES
    courses = Course.objects.filter(id__in=courseIds)

    # print(courses)

    serializer = CourseSerializer(
        courses, many=True)
    # SERIALIZE and return the JSON Response of COURSE List
    return JsonResponse({'List of courses taught by '+emailKey: serializer.data}, safe=False, status=status.HTTP_200_OK)
