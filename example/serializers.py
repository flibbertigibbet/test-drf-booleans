from rest_framework import serializers

from example.models import NoDefault, DefaultTrue, DefaultFalse

class NoDefaultSerializer(serializers.ModelSerializer):
	class Meta:
		model = NoDefault
		fileds = ('name', 'testbool')


class DefaultTrueSerializer(serializers.ModelSerializer):
	class Meta:
		model = DefaultTrue
		fileds = ('name', 'testbool')


class DefaultFalseSerializer(serializers.ModelSerializer):
	class Meta:
		model = DefaultFalse
		fileds = ('name', 'testbool')