from django.urls import path
from . import views
urlpatterns = [
    path('blog/<int:pk>',views.BlogView.as_view()),
    path('blog/',views.BlogView.as_view()),
    
    path('upload/',views.UploadFilesView.as_view())

]