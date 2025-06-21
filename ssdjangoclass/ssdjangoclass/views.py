from django.http import HttpResponse
from django.shortcuts import render

def main(request):
  return render(request, 'website/main.html')

def home(request):
  return HttpResponse("Hello world this is from Home page!")
  # return render(request, 'website/index.html')

def about(request):
  return HttpResponse("Hello world this is from about page!")

def contact(request):
  return HttpResponse("Hello world this is from Contact page!")

def studentss(request):
    student_list = [
        {'name': 'Alice', 'age': 20, 'grade': 'A'},
        {'name': 'Bob', 'age': 22, 'grade': 'B'},
        {'name': 'Charlie', 'age': 21, 'grade': 'A+'},
    ]
    return render(request, 'website/students.html', {'studentss': student_list})

