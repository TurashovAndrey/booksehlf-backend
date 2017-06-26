"""BookShelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from book.views import BookViewSet
from author.views import AuthorViewSet
from travel.views import TravelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet, base_name='book')
router.register('authors', AuthorViewSet, base_name='author')
router.register('travels', TravelViewSet, base_name='travel')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^', include(router.urls))
]
