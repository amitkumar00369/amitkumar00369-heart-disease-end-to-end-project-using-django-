from django.urls import path

from app2.views import userSignup,Login

urlpatterns = [
    path('userSign',userSignup.as_view()),
    path('login',Login.as_view())
]
