from django.shortcuts import render
from .models import User
# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'user/index.html', {"users":users})