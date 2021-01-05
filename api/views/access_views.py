from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import AccessSerializer
from movies.models import Access


class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

