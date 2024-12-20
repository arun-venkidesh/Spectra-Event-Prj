"""
URL configuration for spectraeventprj project.

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
from django.urls import path
from spectraeventapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main, name='main'),
    path('admin/', admin.site.urls),
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('booking/',views.booking, name='booking'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name="contact"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
