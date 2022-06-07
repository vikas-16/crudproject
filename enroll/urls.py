from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home1 ,name="home"),
    path('user/register/',views.signup ,name="register"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),  
    # path('user/Login/',views.Login , name="Login"),
    path('user/login/',views.login_request , name="login"),
    path('user/success/',views.success , name= "success"),
    path('usertoken/', views.token_send, name="token_send"),
    path('addandshow/', views.add_show, name="addandshow"),
    path('view/', views.view_data, name="view_data"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('update/<int:id>/', views.update_data, name="updatedata"),
    # path('emailVerification/<uidb64>/<token>', views.activate, name='emailActivate')

]
