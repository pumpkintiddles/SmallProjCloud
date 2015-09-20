from django.db import models


class JobClient(models.Model):
    job_provider = models.CharField(max_length=200)
    job_provider_address = models.CharField(max_length=200)
    job_provider_contact_name = models.CharField(max_length=200)
    job_provider_contact_phone = models.CharField(max_length=200)
    job_provider_contact_email = models.EmailField()
    job_provider_start_date = models.DateTimeField()
    job_provider_rating = models.IntegerField('Client rating')
    job_provider_project_totals = models.IntegerField('Client total sales/business')
    job_provider_notes = models.CharField(max_length=1000, null=True, blank=True)
    job_provider_conflicts_and_resolution = models.CharField(max_length=2000, null=True, blank=True)
   
    def __str__(self):
	return self.job_provider


class JobDetail(models.Model):
    job_provider = models.ForeignKey('JobClient')
    job_name = models.CharField(max_length=100)
    job_identifier = models.CharField(max_length=100)
    job_refered_by = models.CharField(max_length=100)
    job_contact = models.CharField(max_length=100)
    job_contact_phone = models.IntegerField('Phone')
    job_initiation_date = models.DateTimeField()
    job_sales_person = models.CharField(max_length=100)
    job_projected_start_install_date = models.DateTimeField(null=True, blank=True)
    job_projected_finish_install_date = models.DateTimeField(null=True, blank=True)
    job_initial_deposit_date = models.DateTimeField(null=True, blank=True)
    job_final_drawings_date = models.DateTimeField(null=True, blank=True)
    job_OE_date = models.DateTimeField(null=True, blank=True)
    job_final_install_date = models.DateTimeField(null=True, blank=True)
    job_closed_out_date = models.DateTimeField(null=True, blank=True)
    job_unusual_issues_or_problems = models.CharField(max_length=1000, null=True, blank=True)
    job_print = models.FileField(null=True, blank=True)

    def __str__(self):
	return self.job_name

