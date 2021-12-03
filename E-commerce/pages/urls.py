from django.urls import path

from .views import code, icon

app_name="pages"


urlpatterns = [
    path('', code, name='code'),
    path('', icon, name='icon'),
    
]
