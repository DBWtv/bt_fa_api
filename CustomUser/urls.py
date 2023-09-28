from django.urls import path

from .api import views

api_urls = [
    path('register/', views.RigestrationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.logout_view),
]


urlpatterns = [
    
] + api_urls
