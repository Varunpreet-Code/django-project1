from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('user-details/<int:pk>/', views.UserProfileView.as_view(), name ='userDetails'),
]
