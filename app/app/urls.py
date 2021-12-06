"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import os

from core.views import calculate_age, dame_fecha, saludo, despedida, curso_c, curso_py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('nosveremos/', despedida),
    path('fecha/', dame_fecha),
    path('edades/<int:actual_age>/<int:year>', calculate_age),
    path('curso_c', curso_c),
    path('curso_py', curso_py)
    ]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
