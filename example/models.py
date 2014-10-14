from django.db import models


class NoDefault(models.Model):
	name = models.CharField(max_length=255)
	testbool = models.BooleanField()


class DefaultTrue(models.Model):
	name = models.CharField(max_length=255)
	testbool = models.BooleanField(default=True)


class DefaultFalse(models.Model):
	name = models.CharField(max_length=255)
	testbool = models.BooleanField(default=False)