from django.urls import path
# yazdigimiz functions imporr edirk
from .views import single,products,products1,products2

app_name="product"


urlpatterns = [
    path('single/' ,single, name='single'),
    path('' ,products, name='products'),
    path('' ,products1, name='products1'),
    path('' ,products2, name='products2'),
]
