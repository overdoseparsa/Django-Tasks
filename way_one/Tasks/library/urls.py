from django.urls import path , include

from django.http import HttpResponse

from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet , BookViewSet



router = DefaultRouter()
router.register(r'author' , AuthorViewSet , basename="author" )
router.register(r'book' ,BookViewSet , basename="Book" )


urlpatterns = [
    path('' , include(router.urls))
]
