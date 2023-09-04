"""
URL configuration for empleado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from applications.home.views import IndexView
from applications.departamentos.views import NewDepartamento
from applications.carrito.views import *
from django.conf import settings #importamos los archivos de configuracion de django
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('', include('applications.empleados.urls')),
    path('', include('applications.departamentos.urls')),
     path('', include('applications.carrito.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
