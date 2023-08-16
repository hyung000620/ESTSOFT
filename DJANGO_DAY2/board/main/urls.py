from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout, name='logout'), # 로그아웃
    path("", views.login, name='login'), # 로그아웃
    path("oreumi", views.new_page, name="page"),
    path("oreumi2", views.new_page2, name="page2"),
    path('problem/<int:problem_id>', views.problem, name='page2'),
]