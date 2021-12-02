from django.urls import path
# yazdigimiz functions imporr edirk
from .views import index

app_name="home"


urlpatterns = [
    path('', index, name='index'),
]
