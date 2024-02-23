import factory
from django.contrib.auth.models import User

from blogger.blogapp.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
     
    username = 'x'
    password = 'x'
    is_staff = True 
    is_superuser = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "x"
    subtitle = 'x'
    slug = 'x'
    author = factory.SubFactory(UserFactory)
    content = 'x'
    status = 'Published'