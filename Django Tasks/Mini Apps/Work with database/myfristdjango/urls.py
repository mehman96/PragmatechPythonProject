"""myfristdjango URL Configuration

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
from django.urls import path,include
from index import views
from django.conf.urls.static import static
from django.conf import settings
from index.admin import blog
urlpatterns = [
    path('admin/', admin.site.urls),
    # her app ucun ayri ayri bele admin panel duzelde bilerik
    path('blogadmin/', blog.urls),
    path('', views.index, name='main'),
    #path('blog/<slug:slug>/', views.blog, name='blog'),
    path('blog/', views.blog, name='blog'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.index_title='My Admin Panel'
admin.site.site_header='Admin'