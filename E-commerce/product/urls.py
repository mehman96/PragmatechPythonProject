from django.urls import path
# yazdigimiz functions imporr edirk
from .views import product,products,products1

app_name="product"


urlpatterns = [
    path('' ,product, name='product'),
    path('' ,products, name='products'),
    path('' ,products1, name='products1'),

]
