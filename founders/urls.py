from django.urls import path
from . import views
urlpatterns = [
    path('register_founder/',views.register_founder,name='register_founder'),
]