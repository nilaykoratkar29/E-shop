from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='Shophome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('productview/',views.productview,name='ProductView'),
    path('exp/',views.exp,name='Experiment'),
    path('tshirt/',views.tshirt,name='Tshirt'),

]
