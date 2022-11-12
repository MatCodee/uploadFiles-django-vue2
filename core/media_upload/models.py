from django.db import models

# Create your models here.
class Files(models.Model):
    file = models.FileField(upload_to="files")
    blog = models.ForeignKey('Blog',related_name='files_blog',on_delete=models.CASCADE)

class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField() 
    
    def __str__(self):
        return self.title