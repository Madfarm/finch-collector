from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('finches/', views.finches_index, name="index"),
    path('about/', views.about, name="about"),
    path('finches/<int:finch_id>', views.finches_details, name='details'),
    path('finches/create', views.FinchCreate.as_view(), name="finch_create"),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:finch_id>/add_sighting', views.add_sighting, name='add_sighting'),
    path('finches/<int:finch_id>/assoc_food/<int:food_id>', views.assoc_food, name='assoc_food'),
]