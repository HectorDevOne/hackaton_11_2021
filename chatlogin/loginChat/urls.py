from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from loginChat.views import HomeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'loginChat'

urlpatterns = [
    path('', HomeView.as_view()), 
    path('authtrue/',views.Autenticado.as_view(), name='authtrue' ),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]