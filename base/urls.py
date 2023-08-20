from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('update/<str:pk>/',views.update_list,name="update_list"),
    path('delete/<str:pk>/',views.delete_list,name="delete_list"),
]