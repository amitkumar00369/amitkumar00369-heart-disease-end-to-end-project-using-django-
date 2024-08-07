from django.urls import path
from app1.views import userRegister,LogIn,Predict


urlpatterns = [
    path('userReg',userRegister.as_view()),
    path('Login',LogIn.as_view()),
    path('heartDisease',Predict.as_view())
]
