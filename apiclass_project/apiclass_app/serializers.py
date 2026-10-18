from rest_framework import serializers
from apiclass_app.models import BlogModel



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'
