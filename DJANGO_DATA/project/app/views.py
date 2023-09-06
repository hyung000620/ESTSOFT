from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Company, Student, RandomStudent
from .serializers import CompanySerializer, StudentSerializer
from .forms import StudentForm
import random
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def random_student(request):
    students = Student.objects.all()
    random_student = random.choice(students)
    RandomStudent.objects.create(student=random_student)
    return redirect('random_student_result')

def random_student_result(request):
    random_students = RandomStudent.objects.all()
    random_student = random_students[len(random_students)-1]
    return render(request, "random_student.html", {'random_student': random_student})