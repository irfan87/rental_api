from rest_framework import serializers
from .models import Friend, Belonging, Borrowed

# friends serializer
class FriendSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Friend
        fields = ('id', 'name', 'owner')

# belonging serializer
class BelongingSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Belonging
        fields = ('id', 'name', 'owner')

# borrowed serializer
class BorrowedSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned', 'owner')