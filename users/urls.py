from .views import CustomUserListUpdateDelateAPIView, CustomUserDetailUpdateDelateAPIView, UserRegisterView, \
    CustomUserLogin, LogoutView, ProfileView, ProfileUpdateView
from django.urls import path

app_name = 'users'
urlpatterns = [
    path("user-list/", CustomUserListUpdateDelateAPIView.as_view()),
    path("user-list/<int:pk>", CustomUserDetailUpdateDelateAPIView.as_view()),

    path('register/', UserRegisterView.as_view(), name='regis'),
    path('login/', CustomUserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
]
