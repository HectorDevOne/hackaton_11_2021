from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from loginChat.views import HomeView

app_name = 'loginChat'

urlpatterns = [
    path('', HomeView.as_view()), 
    path('auth/',views.Autenticado.as_view(), name='auth' )
    # path('', TemplateView.as_view(template_name="index.html"), name='home'),
    # path('<int:ind>/<int:can>', views.SliceView.as_view(), name='slice'),
]