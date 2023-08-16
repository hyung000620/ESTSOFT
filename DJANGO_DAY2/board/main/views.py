from django.shortcuts import render
# Create your views here.
items = ["사과","오렌지","수박","메론"]
def index(req):
    is_logined = True
    return render(req, "main/index.html",{"items":items,"is_logined":is_logined,"name":"JunHyung"})

def new_page(req):
    return render(req, "main/oreumi_page.html")

def new_page2(req):
    return render(req, "main/oreumi_page2.html")

def problem(req):
    return render(req, 'problem/{}.html'.format(req.problem_id))

# 로그아웃
def logout(req):
    is_logined = False
    return render(req, "main/index.html",{"items":items,"is_logined":is_logined,"name":"JunHyung"})
def login(req):
    is_logined = True
    return render(req, "main/index.html",{"items":items,"is_logined":is_logined,"name":"JunHyung"})
