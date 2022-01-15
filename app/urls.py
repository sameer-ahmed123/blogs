from django.urls import path
from  . import views
urlpatterns=[
    path('signup',views.signup1,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('',views.blog1,name="blog"),
    path('write',views.writeblog,name='write')
]