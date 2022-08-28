from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class Registration_client_serializer(serializers.Serializer):
    e_mail = serializers.EmailField()
    name = serializers.CharField(max_length=80)
    phone = serializers.CharField(max_length=20)



class CustomUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = super().create(validated_data)
        user.username = user.email
        return user

    def save(self, validated_data):
        print(validated_data)
        user = self.create(validated_data)
        user.save()
        balance = Balance.objects.create(user=user)
        balance.save()
        return user