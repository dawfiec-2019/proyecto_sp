from django.conf.urls import url
from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from .views import lawsViewSet


merouter = merouters.DefaultRouter()
merouter.register(r'laws', lawsViewSet)

urlpatterns = [

]

urlpatterns += merouter.urls