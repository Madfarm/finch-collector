from django.urls import path
from . import views

urlpatterns = [
    path('finches/', views.finches_index, name="index")
]