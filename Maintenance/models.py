from django.db import models

class MaintenanceCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_count = models.IntegerField('Membership total')
    category_initiation = models.DateTimeField(auto_now_add=True)
    category_last_updated = models.DateTimeField(auto_now=True)
    category_discontinued = models.BooleanField()

    def __str__(self):
	return self.category_name

class MaintenanceItem(models.Model):
    category_name_reference = models.ForeignKey('MaintenanceCategory')
    item_name = models.CharField(max_length=100)
    item_id = models.IntegerField('Membership total')
    item_initiation = models.DateTimeField(auto_now_add=True)
    item_last_serviced = models.DateTimeField(auto_now=True)
    item_service_intervals = models.IntegerField('Service Intervals')
    removed_from_service = models.BooleanField()

    def __str__(self):
	return self.item_name
