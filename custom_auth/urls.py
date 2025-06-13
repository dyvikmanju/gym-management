from django.urls import path,include
from custom_auth import views
urlpatterns = [
    path('',views.home ,name="home"),
    path('signup',views.signup ,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('attendance',views.attendance,name="attendance"),
    path('profile',views.profile,name="profile"),

 ]
