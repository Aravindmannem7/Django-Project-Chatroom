from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[

   path('signup',views.signup,name="signup"),
   path('login',views.login,name="login"),
#    path('logout',views.logout,name="logout"),
#    path('register',views.register,name="register"),
#    path('applycr',views.applycr,name="applycr"),
#    path('change',views.change,name="change"),
#    path('review1',views.review1,name="review1"),
#    path('review2',views.review2,name="review2"),
#    path('review3',views.review3,name="review3"),
   


]