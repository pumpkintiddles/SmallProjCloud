from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    def __unicode__(self):
	return self.employee_name
    employee_rank = models.CharField(max_length=100)
    employee_position = models.CharField(max_length=30)
    employee_start_date = models.DateTimeField()
    employee_suspended_date = models.DateTimeField(null=True, blank=True)
    employee_account_closed_date = models.DateTimeField(null=True, blank=True)
    employee_account_reopened_date = models.DateTimeField(null=True, blank=True)
    employee_vacation_left = models.IntegerField('Vacation days left')
    employee_sick_days = models.IntegerField('Sick days left')
    employee_late_days = models.IntegerField('Late days')
    employee_pay_rate = models.IntegerField('Pay rate')
    employee_stats = models.IntegerField('Employee stats')
    employee_awards = models.IntegerField('Employee awards')

