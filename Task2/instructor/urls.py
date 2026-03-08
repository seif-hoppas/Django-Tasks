from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_list, name='instructor_list'),
    path('<int:id>/', views.instructor_detail, name='instructor_detail'),
]