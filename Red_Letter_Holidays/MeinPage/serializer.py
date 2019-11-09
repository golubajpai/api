from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
    	User=super(UserSerializer,self).create(validated_data)
    	User.set_password(validated_data['password'])
    	User.save()
    	
    	return User

class UserObjects(serializers.ModelSerializer):
    class Meta:
    	model=User
    	fields=('first_name','last_name','email','password')



class UserLogin(serializers.Serializer):
	email=serializers.CharField(max_length=20)
	password=serializers.CharField(max_length=20)

	def validate(self,data):
		email=data.get('email')
		password=data.get('password')
		if email and password:
			auth=authenticate(email=email,password=password)
			if auth:
				return auth
			else:
				raise  exceptions.ValidationError('credentials invalid')
		else:
			raise exceptions.ValidationError('fill all the fields')







