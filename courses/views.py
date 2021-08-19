from django import http
from django.shortcuts import render

from django.http import HttpResponse

from . models import Course

# Create your views here.

def index(request):
    #create varible to pull object from database
    courses = Course.objects.all()
    for course in courses:
        print(course.image)
    return render(request, 'courses/index.html',{'courses':courses})



 #mapper this above to url



