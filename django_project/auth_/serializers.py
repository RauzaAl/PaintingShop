from rest_framework import serializers

from django_project.auth_.models import MyUser, Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'role', 'email', 'is_superuser')


class RegisterSerializer(BaseUserSerializer):

    password = serializers.CharField(write_only=True)

    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ('password',)

    def create(self, validated_data):
        password = validated_data.pop('password')

        return MyUser.save_user(validated_data, password)


class UsersSerializer(BaseUserSerializer):

    username = serializers.CharField(read_only=True)
    profile = ProfileSerializer()

    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ('profile',)

    def create(self, validated_data):
        """
        Cannot create User here!
        """
        pass
