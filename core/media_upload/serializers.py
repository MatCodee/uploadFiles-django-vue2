from rest_framework import serializers

from .models import Blog,Files


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['file','blog']
        
        
class BlogSerializer(serializers.ModelSerializer):
    '''
    files_blog = FileSerializer(many=True)
    

    def create(self, validated_data):
        files_element = validated_data.pop('files_blog')
        
        blog = Blog.objects.create(**validated_data)
        for file in files_element:
            Files.objects.create(file=file,blog=blog,**files_element)
        return blog
    '''
    
    class Meta:
        model = Blog
        fields = ['id','title','description']
        
        