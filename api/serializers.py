from rest_framework import serializers
from portal.models import User #, Responsavel

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        #fields = '__all__'
        fields = ('username','password','first_name','last_name')


# class ResponsavelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#
#         model = Responsavel
#         #fields = '__all__'
#         fields = ('registro_responsavel','nome','email')