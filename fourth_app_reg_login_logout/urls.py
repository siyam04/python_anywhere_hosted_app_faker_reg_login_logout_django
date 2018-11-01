from django.urls import path
# Same App importing
from fourth_app_reg_login_logout.views import welcome_user, register, user_login, user_logout

urlpatterns = [

    path('welcome-user', welcome_user, name='welcome-user'),
    path('register', register, name='register'),
    path('user-login', user_login, name='user-login'),
    path('user-logout', user_logout, name='user-logout'),


]

