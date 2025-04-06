from django.urls import path
from .views import create_stadion, get_all_stadions, get_stadion, update_stadion, delete_stadion, get_all_order

urlpatterns = [
    path('create_stadion/', create_stadion, ),
    path('get_all_stadions/', get_all_stadions, ),
    path('get_stadion/<int:pk>/', get_stadion, ),
    path('update_stadion/<int:pk>/', update_stadion, ),
    path('delete_stadion/<int:pk>/', delete_stadion, ),
    path('get_all_order/', get_all_order, ),


]
