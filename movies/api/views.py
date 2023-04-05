from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from .models import movies
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class MovieList(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data=movies)
    def post(self,request,*args,**kwargs):
        data=request.data
        movies.append(data)
        return Response(data=movies)

class MovieItem(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        movie=[i for i in movies if i['id']==id].pop()
        # for i in movies:
        #     if i['id']==id:
        #         movie=i
        return Response(data=movie)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        data=request.data
        movie=[i for i in movies if i['id']==id].pop()
        movie.update(data)
        return Response(data=movies)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        movie=[i for i in movies if i['id']==id].pop()
        movies.remove(movie) 
        return Response(data=movies)
    
class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"registeration completed"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
