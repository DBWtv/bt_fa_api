from django.urls import path
from .api.views import MessageView, MessageHistory

api_urls = [
    path('message/', MessageView.as_view()),
    path('message/history/', MessageHistory.as_view()),
]

urlpatterns = [
    
] + api_urls
