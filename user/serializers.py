from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        min_length=6,
        write_only=True,
        required=True
    )
    email = serializers.EmailField()

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate_email(self, email):
        email_exist = (
            User.objects.filter(email=email).exists()
        )
        if email_exist:
            raise serializers.ValidationError(
                'Such email is already used. Please, try another one'
            )

        return email

    def validate_username(self, username):
        user_exist = (
            User.objects.filter(username=username).exists()
        )
        if user_exist:
            raise serializers.ValidationError(
                'Such username already exists. Please, try another one'
            )
        return username


class UserListSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['id', 'username']
