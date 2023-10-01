from django.urls import path
from .api.views import MessageView

api_urls = [
    path('message/', MessageView.as_view()),
]

urlpatterns = [
    
] + api_urls
