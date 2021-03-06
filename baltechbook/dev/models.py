from __future__ import unicode_literals
from django.db import models
from invoice.constants import WEBPAGE_REF

# Service request from dev
class request_service_table(models.Model):
    request_service_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=200)
    webpage_ref = models.CharField(max_length=18, choices=WEBPAGE_REF)
    description = models.TextField()
    user_status_is_done = models.BooleanField(default=0)
    dev_status_is_done = models.BooleanField(default=0)
    report_date = models.DateTimeField(auto_now=True)
    service_completion_date = models.DateTimeField()

    class Meta:
        verbose_name = "Service Request"
        verbose_name_plural = "Service Requests"

