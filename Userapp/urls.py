from django.urls import path
from Userapp.views import user_logout,user_login,user_register,userprofile,user_update,user_password,usercomment,comment_delete



urlpatterns = [
    path('signin/',user_login,name='user_login'),
    path('register/',user_register, name='user_register'),
    path('signout/',user_logout,name='user_logout'),
    path('profile/', userprofile, name='userprofile'),
    path('user_update/',user_update , name='user_update'),
    path('user_passwordupdate/', user_password, name='user_password'),
    path('usercomment/',usercomment,name='usercomment'),
    path('user_comment_delete/<int:id>/',comment_delete, name="comment_delete")


]
