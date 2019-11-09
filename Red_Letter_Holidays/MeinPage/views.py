from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from .serializer import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login ,logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

UserModel = get_user_model()
from rest_framework import generics

           #
class Data(APIView):
	permission_classes = (IsAuthenticated,)  
	def get(self,request):
		data=User.objects.all()
		name= UserObjects(data, many=True)
		return Response(name.data)

class UserCreateAPIView(generics.CreateAPIView):
	serializer_class = UserSerializer

	def create(self, request, *args, **kwargs):
		
		serializer=self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		
		token, created = Token.objects.get_or_create(user=serializer.instance)
		return Response({'token': token.key,'message':"User logged in successfully"
}, status=status.HTTP_201_CREATED)
		

class Logout(LoginRequiredMixin,APIView):
    permission_classes = (IsAuthenticated,)  
    def get(self, request, format=None):
        # simply delete the token to force a login
        logout(request.user)
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)	


class Login(APIView):
	permission_classes = (IsAuthenticated,) 



	def post(self,request):

		serelize=UserLogin(data=request.data)
		serelize.is_valid(raise_exception=True)
		objectuser=serelize.validated_data
		login(request,objectuser)
		token, _ = Token.objects.get_or_create(user=objectuser)
		return Response({'token':token.key})
