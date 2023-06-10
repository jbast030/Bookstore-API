from django.urls import path
from .views import test_view

# add route paths here
urlpatterns = [
    path('test/', test_view),
]
