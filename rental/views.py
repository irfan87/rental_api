from rest_framework import viewsets

from .models import Friend, Belonging,Borrowed
from .serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer
from .permissions import IsOwner

# friends viewsets that attached to model and serializers
class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.all()

    serializer_class = FriendSerializer

    permission_classes = [IsOwner]

# belonging viewsets and borrowed serializers that do the same ways as friends viewsets that attached to models and serializers
class BelongingViewset(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()

    serializer_class = BelongingSerializer

    permission_classes = [IsOwner]

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()

    serializer_class = BorrowedSerializer

    permission_classes = [IsOwner]
