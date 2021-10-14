from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginScreen, name='login'),
    path('register/', views.registerScreen, name='register'),
    path('iris/', views.IrisViewSet.iris_list),
    path('iris/<int:pk>/', views.IrisViewSet.iris_detail),
]