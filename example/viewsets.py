from rest_framework.viewsets import ModelViewSet

from example.models import NoDefault, DefaultTrue, DefaultFalse
from example.serializers import NoDefaultSerializer, DefaultTrueSerializer, DefaultFalseSerializer

class NoDefaultViewSet(ModelViewSet):
	queryset = NoDefault.objects.all()
	serializer_class = NoDefaultSerializer


class DefaultTrueViewSet(ModelViewSet):
	queryset = DefaultTrue.objects.all()
	serializer_class = DefaultTrueSerializer


class DefaultFalseViewSet(ModelViewSet):
	queryset = DefaultFalse.objects.all()
	serializer_class = DefaultFalseSerializer