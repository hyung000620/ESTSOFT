from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'app/article_list.html',{'articles':articles})

def article_create(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        
        Article.objects.create(title=title, content=content)
        return redirect('article_list')
    
    return render(request, 'app/article_create.html')

def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article_list')
    else:
        form = UserCreationForm()    
    return render(request, 'app/register.html', {'form':form})