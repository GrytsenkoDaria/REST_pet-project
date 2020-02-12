from rest_framework import serializers
from user.models import Profile
from choices import Role, UserStatus


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.RelatedField(source='profile', read_only=True)
    role = serializers.ChoiceField(choices=Role.choices)
    status = serializers.ChoiceField(choices=UserStatus.choices)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.role = validated_data.get('role', instance.role)
        instance.status = validated_data.get('status', instance.status)

        instance.save()
        return instance


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'
