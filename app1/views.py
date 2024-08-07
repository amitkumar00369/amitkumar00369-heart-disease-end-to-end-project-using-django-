from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from app1.serializers import SqlSerializer,HelthSerializer
from app1.models import SqlTable,SQLToken
import jwt,datetime
from dotenv import load_dotenv
import pickle
load_dotenv()
import os
secret=os.getenv('secret')
print(secret)

class userRegister(APIView):
    def post(self,request):
       
        try:
            serializer=SqlSerializer(data=request.data)
            if serializer.is_valid():
                user=serializer.save()
                return Response({'message':"Successs",'data':serializer.data},200)
            
            else:
                return Response({"message":serializer.errors},400)
        except Exception as e:
            return Response(str(e),500)
        
class LogIn(APIView):
    def post(self,request):
        try:
            email=request.data.get('email')
            if not email or '@' not in email or '.' not in email:
                return Response({'message':"Enter valid email"},400)
            password=request.data.get('password')
            if not password:
                return Response({'message':"Enter password"})
            user=SqlTable.objects.filter(email=email).first()
            if not user:
                return Response({'message':"please signup firstly then visit on login page, Thank you"})
            if not check_password(password,user.password):
                return Response({'message':"Your Password is wrong"})
            payload={
                'id':user.id,
                'exp':datetime.datetime.utcnow()+datetime.timedelta(days=1),
                'iat':datetime.datetime.utcnow()
            }
            token=jwt.encode(payload,secret,algorithm='HS256')
            access_token=SQLToken.objects.create(userId=user.id,email=user.email,token=token)
            return Response({'message':"User login Successfully",'email':user.email,
                             'token':token
                             },200)
            
                
        
        except Exception as e:
            return Response(str(e))
        
class Predict(APIView):
    def post(self,request):
        try:
            token=request.headers.get('Authorization')
            if not token:
                return Response({'message':"Enter token"})
            # print(token)
            decode=jwt.decode(token,secret,algorithms=['HS256'])
            print(decode)
            id=decode['id']
            user=SQLToken.objects.filter(token=token,userId=id)
            if not user:
                return Response({'message':"session of user not active"})
            with open('myModel.pkl', 'rb') as file:
                loaded_model = pickle.load(file)
            serializer=HelthSerializer(data=request.data)
            print("hello")
            if serializer.is_valid():
                data=serializer.save()
                result=loaded_model.predict([[data.age,data.sex,data.cp,data.trestbps,data.chol,data.fbs,
                                              data.restecg,data.thalach,data.exang,data.slope,data.ca,data.thal,
                                              data.new_oldpeak]])
                print(result)
                data.result=result
                data.save()
                return Response({'message':"prediction",'data':serializer.data})
        except jwt.ExpiredSignatureError as e:
            return Response(str(e))
        except jwt.InvalidTokenError as e:
            return Response(str(e))
            
            
                
        except Exception as e:
            return Response({'message':str(e)},500)