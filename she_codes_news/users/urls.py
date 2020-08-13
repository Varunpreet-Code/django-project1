from django.urls import path
from . import views
from .views import AuthorView

app_name = 'users'
urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('user-details/<int:pk>/', views.UserProfileView.as_view(), name ='userDetails'),
    path('author-view/<int:pk>/', AuthorView.as_view(), name = 'authorView'),
]

