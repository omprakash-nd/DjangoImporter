from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ControlPlan(models.Model):
	PartNo_PartName = models.CharField(max_length=100)
	SupplierCode = models.CharField(max_length=100)
	SupplierName = models.CharField(max_length=30)
	ControlPlanVersion = models.IntegerField()
	PDIPlanVersion = models.CharField(max_length=30)
	Uploaded_on = models.CharField(max_length=30)
	Download_Upload = models.CharField(max_length=10)

	def __unicode__(self):
		return ('%r')%(self.PartNo_PartName)
