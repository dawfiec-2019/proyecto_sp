from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsts
from .serializer import lawsSerializer
from .models import laws
# Create your views here.
class lawsViewSet(meviewsts.ModelViewSet):
    lookup_field = 'id'
    queryset = laws.objects.all()
    serializer_class = lawsSerializer