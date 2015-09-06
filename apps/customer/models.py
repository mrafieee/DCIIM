from django.db import models
from django.utils.translation import ugettext_lazy as _

SERVICE_TYPE = (
    ('vpc', _('Virtual Private Cloud (VPC)')),
    ('vps', _('Virtual Private Server (VPS)')),
    ('dc', _('Datacenter')),
    ('saas', _('SaaS')),
)

class Customer(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    contact_point_full_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    cell_phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    national_code = models.CharField(max_length=100, blank=True, null=True)
    service_type = models.CharField(max_length=100, blank=True, null=True, choices=SERVICE_TYPE)
    website_url = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

