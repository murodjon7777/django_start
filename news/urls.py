from django.urls import path
from .views import Uy
urlpatterns = [
    
    path('',Uy.as_view(), name='home')
]
