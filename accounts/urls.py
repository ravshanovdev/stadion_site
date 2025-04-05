from django.urls import path
from .views import RegisterApiView, CustomTokenObtainPairApiView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), ),
    path('login/', CustomTokenObtainPairApiView.as_view(), ),
    path('refresh_token/', TokenRefreshView.as_view(), ),

]

