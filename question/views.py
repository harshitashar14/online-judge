from django.shortcuts import render
from ojuser.models import Ojuser
from django.contrib.auth.models import User
from .serializers import QuestionSerializer, FileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Question
import os.path, uuid, subprocess


# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def getQuestion(request):
    try:
        question = Question.objects.get(id =request.query_params.get('id'))
    except ObjectDoesNotExist:
        return JsonResponse({
            'status' : 'failed',
            'code' :404,
            'Error Message': 'Question not Found!'
            })
    
    return JsonResponse({
        'status': 'succeded',
        'code': 200,
        'data': question,
        })
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createQuestion(request):
    serializer= QuestionSerializer(data= request.data)
    serializer.is_valid(raise_exception= True)
    print(request.user.username)
    print(type(request.user))
    ojuser = Ojuser.objects.get(username = request.user.username)
    question = Question.objects.create(**serializer.data)
    question.creator = request.user
    question.save()
    return JsonResponse({
        'status': 'succeded',
        'code': 200,
    
        })

dirame = os.getcwd()
dirCodes = os.path.join(dirame, 'codes')
if os.path.isdir(dirCodes) == False:
    os.mkdir(dirCodes)

@api_view(['POST'])
@permission_classes([AllowAny])
def createFile(request):
    print(request.data['language'])
    language = request.data['language']
    code = request.data['code']
    print('1')
    jobId = uuid.uuid4().hex
    jobId = jobId + '.' + language
    filepath = os.path.join(dirCodes, jobId)
    f = open(filepath, 'w')
    f.write(code)
    print(filepath)
    return JsonResponse({'status':'succeeded', 
     'code':200, 
     'data':filepath})


dirOutputs = os.path.join(dirame, 'outputs')
if os.path.isdir(dirOutputs) == False:
    os.mkdir(dirOutputs)

@api_view(['POST'])
@permission_classes([AllowAny])
def runCppFile(request):
    filepath = request.data['filepath']
    jobId = os.path.basename(filepath).split('.')[0] + '.' + 'out'
    outPath = os.path.join(dirOutputs, jobId)
    outPutt = os.path.join(dirOutputs, 'o.outp')
    myop = open(outPutt, 'w')
    cmd = ['g++ ' + filepath + ' -o ' + outPath + ' && cd ' + dirOutputs + ' && ./' + jobId]
    cmd1 = ['ls']
    try:
        status = subprocess.run(cmd, timeout=60, shell=True, check=True, stdout=myop)
        print(status.stdout)
        return JsonResponse({'status':'succeeded', 
         'code':200, 
         'data':'done'})
    except subprocess.TimeoutExpired:
        print('Failed')
        return JsonResponse({'status':'succeeded', 
         'code':200, 
         'data':'Failed'})
