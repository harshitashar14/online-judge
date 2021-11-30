from django.urls import path
from .views import createQuestion,getQuestion,createFile,runCppFile
urlpatterns = [
    path('create', createQuestion),
    path('get', getQuestion),
    path('createFile', createFile),
    path('runCpp', runCppFile)
]
