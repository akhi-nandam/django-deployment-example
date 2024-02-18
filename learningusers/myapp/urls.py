from django.urls import re_path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    re_path(r'^registration/',views.register,name="registration"),
    re_path(r'^user_login/$',views.user_login,name="user_login"),
]