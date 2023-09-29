from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


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

@csrf_exempt
def get(request):
    print(request.headers)
    return HttpResponseBadRequest()