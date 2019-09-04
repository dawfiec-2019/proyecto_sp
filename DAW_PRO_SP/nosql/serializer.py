from rest_framework_mongoengine import serializers
from .models import laws



class lawsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = laws
        fields = '__all__'
