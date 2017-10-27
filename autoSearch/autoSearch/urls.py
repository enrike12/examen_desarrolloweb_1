"""autoSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from carros import views
from carros.views import car_list, car_detail, home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home, name='home.html'),
    url(r'^car_list$',car_list.as_view(),name='car_list'),
    url(r'^car_detail/(?P<id>[0-9]+)/$', car_detail.as_view(), name='car_detail'),


 ] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
