from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apiclass_app.serializers import *
from apiclass_app.models import *


from django.shortcuts import get_object_or_404



class BlogAPIview(APIView):
    def get(self, request):
        blog_data = BlogModel.objects.all()
        serializer_data = BlogSerializer(blog_data, many=True)
        return Response({
            'success':True,
            'message': 'Data Found',
            'data': serializer_data.data,
        }, status=status.HTTP_200_OK)




    def post(self, request):
        serializer_data = BlogSerializer(data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                'success':True,
                'message': 'Blog Created Sucessfully',
                'data': serializer_data.data,

            })
        else:
            return Response({
                'success': False,
                'message' : serializer_data.errors

            })




class BlogDetail(APIView):
    def get_object(self, id):
        try:
            data = get_object_or_404(BlogModel, id=id)
            return data
        except BlogModel.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Data Not Found',
                'data':[]   
            })

    def get(self, request, id):
        blog_data = self.get_object(id)
        serializer_data = BlogSerializer(blog_data)
        return Response({

            'success':True,
            'message': 'Blog get',
            'data': serializer_data.data,
        })  


    def delete(self , request, id):
        self.get_object(id).delete()
        return Response({
              'success': True,
                'message': 'Blog Delete',
                'data':[]   
            
        })  


    def put(self, request, id):
        blog_data = self.get_object(id)
        serializer_data = BlogSerializer(blog_data, data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                
            'success':True,
            'message': 'Blog Update Successfully',
            'data': serializer_data.data,

            })


        else:
            return Response({
                'success':False,
                'message': serializer_data.errors,
                
            })
              



        