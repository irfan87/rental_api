from rest_framework import serializers
from .models import Friend, Belonging, Borrowed

# friends serializer
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'name')

# belonging serializer
class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belonging
        fields = ('id', 'name')

# borrowed serializer
class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')