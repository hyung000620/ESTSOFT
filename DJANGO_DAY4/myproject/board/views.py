from django.shortcuts import render,redirect
from .models import Post

def read_Post_data(request):
    posts = Post.objects.all()
    return render(request, "board/index.html", {"posts": posts})

def add_Post_data(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        published_date = request.POST['published_date']
        
        post = Post(title=title, content=content, published_date = published_date)
        post.save()
        return redirect('index')
    
    return render(request, "board/add_page.html")