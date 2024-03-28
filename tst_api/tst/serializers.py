from rest_framework import serializers
from .models import Tst, Page

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'supervisor', 'document']

class TstSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)

    class Meta:
        model = Tst
        fields = ['editor', 'cover', 'month', 'pages']
