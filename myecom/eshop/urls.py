from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('exp/',views.exp,name='Experiment'),
    path('tshirt/',views.tshirt,name='Tshirt'),
    path('index/',views.productview,name='productspage'),
]
