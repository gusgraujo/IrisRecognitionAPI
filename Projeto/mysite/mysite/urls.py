from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('iris.urls')),
    path('admin/', admin.site.urls),
]