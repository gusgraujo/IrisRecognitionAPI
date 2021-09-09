from rest_framework import serializers
from iris.models import Iris


class IrisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iris
        fields  = ['id','nome','usuario','password','data_registro']

