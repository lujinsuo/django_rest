#-*-coding:utf-8-*-
#作者：test
#创建时间： 2019/8/19 15:10
#文件：  serializers.PY
from django.contrib.auth.models import User,Group
from rest_framework import serializers
from api01.models import Event,Guest


class UserSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields=('url','username','email','groups')


class GroupSerilizers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Group
		fields=('url','name')


class EventSerilizers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Event
		fields=('name','address','start_time','limit','status')


class GuestSerilizers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Guest
		fields=('realname','phone','email','sign','create_time','event_id')

