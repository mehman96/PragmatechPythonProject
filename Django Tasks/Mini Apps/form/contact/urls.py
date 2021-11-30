from django.urls import path
from .views import contact
from django.conf import settings
from django.urls import path,re_path
from django.views.static import serve

app_name='contact'

urlpatterns = [
    path('', contact, name='contact'),
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    
] 
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)