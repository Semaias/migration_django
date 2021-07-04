from django.urls import path
from .views import someview, anyview

urlpatterns = [
    path('get', someview, name="someview"),
    path('post', anyview, name="anyview"),
]
