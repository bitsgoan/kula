import uuid

from base.models import ShortenURL
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response  # returns in json format

from .serializers import URLSerializer

# Create your views here.

@api_view(['POST'])
def convert(request):
	full_url = request.data['url']
	unique_id = str(uuid.uuid4())[:7]
	new_url = ShortenURL(full_url = full_url, uuid = unique_id)
	new_url.save()
	return_dict = {"shortened_url" : "http://127.0.0.1:8000/"+ str(new_url) }
	return Response(return_dict)

@api_view(['GET'])
def listall(request):
	items = ShortenURL.objects.all()
	serializer = URLSerializer(items, many = True)
	return Response(serializer.data)


@api_view(['GET'])
def list(request, pk):
	try:
		items = ShortenURL.objects.get(uuid = str(pk))
		serializer = URLSerializer(items, many = False)
		return Response(serializer.data["full_url"])
	except ShortenURL.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	except:
		return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def delete(request, pk):
	try:
		items = ShortenURL.objects.get(uuid = str(pk))
		serializer = URLSerializer(items, many = False)
		items.delete()
		return Response(status = status.HTTP_200_OK)
	except ShortenURL.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

def home(request):
	return HttpResponse("Home")
