from django.urls import path
from .api.views import TokenView

api_urls = [
    path('token/', TokenView.as_view()),
]

urlpatterns = [
    
] + api_urls
