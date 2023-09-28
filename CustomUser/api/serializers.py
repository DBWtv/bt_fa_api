from rest_framework import serializers
from CustomUser.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = (
            'id',
            'is_superuser',
            'is_staff',
        )
        write_only_fields = ('password',)

    def create(self, validated_data):
        instance = CustomUser.objects.create_user(**validated_data)
        return instance
