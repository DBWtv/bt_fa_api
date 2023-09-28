from django.urls import path
from .api import views

api_urls = [
    path('bot/<str:token>', views.TgBotView.as_view()),
]

urlpatterns = [
    
] + api_urls
