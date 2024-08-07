from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from rest_framework.views import APIView
from app2.models import  MongoTable,MongoToken
from rest_framework import status
from rest_framework.response import Response
import jwt,datetime
from dotenv import load_dotenv
load_dotenv()
import os
secret=os.getenv('secret')
print(secret)

class userSignup(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            if not name:
                return Response({'message': "Enter name"}, status=status.HTTP_400_BAD_REQUEST)
            
            email = request.data.get('email')
            if not email or '@' not in email or '.' not in email:
                return Response({'message': "Enter valid email"}, status=status.HTTP_400_BAD_REQUEST)
            
            password = request.data.get('password')
            if not password:
                return Response({'message': "Enter password"}, status=status.HTTP_400_BAD_REQUEST)
            
            hash_password = make_password(password=password)
            find=MongoTable.objects.filter(email=email).first()
            if find:
                return Response({'message': "User already registered"}, status=status.HTTP_409_CONFLICT)
            
            user = MongoTable.objects.create(name=name, email=email, password=hash_password)
            
            return Response({'message': "Created successfully", 'data': {'id': str(user.id), 'name': user.name, 'email': user.email}}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response(str(e))
class Login(APIView):
    def post(self,request):
        try:
            email=request.data.get('email')
            if not email or '@' not in email or '.' not in email:
                return Response({'message':"Enter valid email"},400)
            password=request.data.get('password')
            if not password:
                return Response({'message':"Enter password"})
            print('comes')
            user=MongoTable.objects.filter(email=email).first()
            print("common",user.id)
            if not user:
                return Response({'message':"please signup firstly then visit on login page, Thank you"})
            if not check_password(password,user.password):
                return Response({'message':"Your Password is wrong"})
            payload={
                'id':str(user.id),
                'exp':datetime.datetime.utcnow()+datetime.timedelta(days=1),
                'iat':datetime.datetime.utcnow()
            }
            print('payload',payload)
            token=jwt.encode(payload,secret,algorithm='HS256')
            print('token',token)
            print("yaha aa gaye")
            access_token=MongoToken.objects.create(userId=str(user.id),email=user.email,token=token)
            return Response({'message':"User login Successfully",'email':email,
                             'token':token
                             },200)
            
                
        
        except Exception as e:
            return Response(str(e))
                
       