"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from schema_graph.views import Schema
from django.shortcuts import redirect

def redirect_to_external(request):
    return redirect('https://final-project-db-tan.vercel.app/')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Bakery.urls')), # Add this line
    path('schema/', Schema.as_view()),
    path('', redirect_to_external)
]
