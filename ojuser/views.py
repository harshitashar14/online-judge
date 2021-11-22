from django.shortcuts import render
from ojuser.models import Ojuser
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(request.data)
    user.save()
    return JsonResponse({
        'status': 'succeded',
        'code': 200,
    })