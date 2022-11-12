from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog,Files
from .serializers import BlogSerializer,FileSerializer
from django.http import JsonResponse

class BlogView(APIView):
    def get(self,request,pk=None,*args, **kwargs):
        blog = Blog.objects.filter(id=pk).first()
        serializer = BlogSerializer(blog)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def post(self,request,pk=None,*args, **kwargs):
        data = request.data
        print(data)
        if data:
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        return JsonResponse({'message': 'no-data'})
        
        
# Esta funcion n vale para ndada no funciona
class UploadFilesView(APIView):
    def post(self,request):
        #file_element = Files(file=request.FILES['file'])
        print(request.data)        
        file_serializer = FileSerializer(data=request.data)
        print(file_serializer.is_valid())
        print(file_serializer.errors)
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse({'message': 'save'})
        else:
            return JsonResponse({'message': 'error'})
        
'''
class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = FileListSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=Photo.objects.all()
'''