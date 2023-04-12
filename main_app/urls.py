from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('finches/', views.finches_index, name="index"),
    path('about/', views.about, name="about"),
    path('finches/<int:finch_id>', views.finches_details, name='details')
]