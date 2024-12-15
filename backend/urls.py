
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('react_app/', include('react_app.urls')),
]
