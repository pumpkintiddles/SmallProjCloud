from django.db import models

class PotentialJobProvider(models.Model):
    potential_job_provider = models.CharField(max_length=200)
    potential_job_provider_address = models.CharField(max_length=200)
    potential_job_provider_contact_name = models.CharField(max_length=200)
    potential_job_provider_contact_phone = models.CharField(max_length=200)
    potential_job_provider_contact_email = models.EmailField(null=True, blank=True)
    potential_job_provider_notes = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
	return self.potential_job_provider
