from django.urls import path 
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<int:sno>', views.deletefriend, name="deletefriend"),
    path('update/<int:sno>', views.updatefriend, name="updatefriend"),
    path('signup', views.signupUser, name="signupUser"),
    path('login', views.loginUser, name="loginUser"),
    path('logout', views.logoutUser, name="logoutUser"),
]