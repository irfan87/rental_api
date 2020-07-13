from rest_framework import viewsets

from .models import Friend, Belonging,Borrowed
from .serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer

# friends viewsets that attached to model and serializers
class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.all()

    serializer_class = FriendSerializer

# belonging viewsets and borrowed serializers that do the same ways as friends viewsets that attached to models and serializers
class BelongingViewset(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()

    serializer_class = BelongingSerializer

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()

    serializer_class = BorrowedSerializer
