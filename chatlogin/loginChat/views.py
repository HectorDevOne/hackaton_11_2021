from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

class Autenticado(APIView):
    def get(self, request):
        data = {"estado": 'Autenticado'}
        return Response(data)

