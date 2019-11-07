from django.shortcuts import render

from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from api01.serializers import UserSerializers,GroupSerilizers
from api01.serializers import EventSerilizers,GuestSerilizers
from api01.models import  Event,Guest
from django.http import HttpResponse,request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from api01.models import Event,Guest
from rest_framework.parsers import JSONParser
from rest_framework import  status,response
from rest_framework.decorators import  api_view

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerilizers


# class EventViewSet(viewsets.ModelViewSet):
# 	queryset=Event.objects.all()
# 	serializer_class = EventSerilizers

class JSONResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		content=JSONRenderer.render(data)
		print(data)
		kwargs['content_type']='application/json'
		super(JSONResponse,self).__init__(content,**kwargs)

@api_view(['GET','POST'])
@csrf_exempt
def event_list(request):
	if request.method=='GET':
		res=Event.objects.all()
		serializer=EventSerilizers(res,many=True)
		print(serializer)
		return JSONResponse(serializer.data)
	elif request.method=='POST':
		data=JSONParser().parse(request)
		serializer=EventSerilizers(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data,status=201)

		return JSONResponse(serializer.errors,status=400)

@api_view(['GET','PUT','DELETE'])
def event_deail(request,pk):
	try:
		res=Event.objects.get(pk=pk)
	except res.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)
	if request.method=='GET':
		serializer=EventSerilizers(res)
		return JSONResponse(serializer.data)
	elif request.method=='PUT':
		data=JSONParser().parse(request)
		serializer=EventSerilizers(res,data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	elif request.method=='DELETE':
		res.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)




