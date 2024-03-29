from rest_framework import  serializers, generics
from django.contrib.auth.models import User
from .models import Post, Comment
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']

class UserSerializerDetail(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post-detail',
        many=True,
        read_only=True
    )
    comments = serializers.HyperlinkedRelatedField(
        view_name='post-comments',
        many=True,
        read_only=True
    )
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'posts', 'comments']

 
class CommentSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    post = serializers.HyperlinkedRelatedField(
        view_name='post-detail',
        read_only=True
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )
    post_id = serializers.SerializerMethodField('get_posts')
    class Meta:
        model = Comment
        fields = [ 'content', 'user', 'created', 'post_id', 'post']    
    
    def get_posts(self, obj):
        return obj.post.id
 
class PostSerializer(serializers.HyperlinkedModelSerializer):
    # comments = serializers.StringRelatedField(many=True)
    comments = serializers.HyperlinkedRelatedField(
        view_name='post-comments',
        many=True,
        read_only=True
    )
    user = UserSerializer(read_only=True)
    #user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Post
        fields = ['url','title','user', 'content', 'created', 'comments']


from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

'''
class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

'''

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    username = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user

from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer


class LoginSerializer(RestAuthLoginSerializer):
    username = None
    first_name = None
    last_name = None
