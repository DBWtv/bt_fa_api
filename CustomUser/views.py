from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'token': request.user.chat_token
            }
            return render(request, 'index.html', context)
        return render(request, 'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'register.html')