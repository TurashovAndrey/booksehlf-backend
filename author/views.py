from .models import Author
from .serializers import AuthorSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
