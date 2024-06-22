from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('contact/', Contact.as_view(), name="contact"),
    path('thanks/', thanks, name="thanks"),

]
