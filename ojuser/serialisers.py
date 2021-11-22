from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length = 20, required = True),
    last_name = serializers.CharField(max_length= 20, required = True),
    username = serializers.CharField(max_length= 20, required = True),
    password = serializers.CharField(max_length= 20, required = True),
    email = serializers.CharField(max_length= 40),