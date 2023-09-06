from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('list', views.student_list, name="student_list"),
    path('add', views.add_student, name="add_student"),
    path('random', views.random_student, name="random_student"),
    path('random/result', views.random_student_result, name="random_student_result"),

]