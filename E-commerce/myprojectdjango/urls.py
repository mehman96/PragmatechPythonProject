
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include("home.urls",namespace="home"),),
    path('product/',include("product.urls",namespace="product"),),
    path('products/',include("product.urls",namespace="products"),),
    path('products/',include("product.urls",namespace="products1"),),
    path('about/',include("about.urls",namespace="about"),),
    path('contact/',include("contact.urls",namespace="contact"),),
    path('code/',include("pages.urls",namespace="code"),),
    path('icon/',include("pages.urls",namespace="icon"),),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
