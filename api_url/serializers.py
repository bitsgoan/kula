from base.models import ShortenURL
from rest_framework import serializers


class URLSerializer(serializers.ModelSerializer):
	class Meta:
		model = ShortenURL 
		fields = '__all__'
		extra_kwargs = {'uuid': {'allow_null': True, 'required': False}}
