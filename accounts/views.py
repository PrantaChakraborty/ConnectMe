from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            user = authenticate(username=request.POST.get['username'],
                                password=request.POST.get['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Account Disable')
            else:
                return HttpResponse('Invalid Login')

    return request(request, 'accounts/login.html')
