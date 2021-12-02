from django.urls import path
# yazdigimiz functions imporr edirk
from .views import product

app_name="product"


urlpatterns = [
    path('' ,product, name='product'),
]
