from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# ORM Object Relational Mapping (ORM) is a technique that allows developers to interact with a database using an object-oriented paradigm. In Django, the ORM provides a way to define models as Python classes, which are then mapped to database tables. This abstraction simplifies database operations by allowing developers to work with high-level objects instead of writing raw SQL queries.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password"]
        extra_kwargs={'password': {'write_only': True}}

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=['id','title','content','created_at','author']
        extra_kwargs={'author': {'read_only': True}}
    
