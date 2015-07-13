from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

USER_ROLE_CHOICES = (
    ('member', 'Member'),
    ('admin', 'Administrator'),
    ('keystone admin', 'Keystone Admin'),
)

RAID_CHOICES = (
    ('raid0', 'RAID 0'),
    ('raid1', 'RAID 1'),
    ('raid5', 'RAID 5'),
    ('raid1+0', 'RAID 1 + 0'),
    ('softwareraid5', 'Software RAID 5'),
)

VLAN_CHOICES = (
    ('trunk', 'Trunk'),
    ('vlan90', 'Vlan 90'),
    ('vlan91', 'Vlan 91'),
    ('valn92', 'Vlan 92'),
    ('vlan93', 'Vlan 93'),
    ('vlan94', 'Vlan 94'),
    ('vlan95', 'Vlan 95'),
)

NET_TYPE_CHOICES = (
    ('vlan', 'vlan'),
    ('local', 'Local'),
    ('flat', 'Flat'),
    ('xvlan', 'XVLAN'),
    ('gre', 'GRE'),
)

HYPERVISOR_CHOICES = (
    ('kvm', 'KVM'),
    ('qemu', 'Qemu'),
    ('docker', 'Docker'),

)
######################################################################

# class User(models.Model):
#     name = models.CharField(_('User full name'), max_length=100, blank=False)
#     email = models.CharField(max_length=100, blank=False)
#     project = models.ForeignKey(Project)
#     role = models.CharField(max_length=100, blank=False, choices=USER_ROLE_CHOICES, default="member")
#
#     def __unicode__(self):
#         return self.name
#
# class Customer(models.Model):
#     user = models.ForeignKey(User)
#     contract_date = models.DateTimeField(default=datetime.now())
#     phone = models.CharField(max_length=100, blank=False)
#     secondary_email = models.CharField(max_length=100, blank=True, null=True)
#     address = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#
#     def __unicode__(self):
#         return self.user
#
#
# class Project(models.Model):
#     name = models.CharField(_('Project Name'), max_length=300, blank=False, help_text=_('Project / Tenant name'))
#     tenant_id = models.CharField(max_length=100, blank=True, null=True)
#     start_date = models.DateTimeField(default=datetime.now())
#     stop_date = models.DateTimeField(blank=True, null=True)
#     owner = models.ForeignKey(Customer)
#     description = models.TextField(blank=True, null=True)
#     resources = models.TextField(blank=True, null=True)
#
#     def __unicode__(self):
#         return self.name
#
# class Network(models.Model):
#     project = models.ForeignKey(Project)
#     name = models.CharField(_('Network name'), max_length=100, blank=False)
#     network = models.CharField(max_length=100, blank=False)
#     netmask = models.CharField(max_length=100, blank=False)
#     type = models.CharField(max_length=100, blank=False, choices=NET_TYPE_CHOICES, default="local")
#     gateway = models.CharField(_('Gateway IP address'), max_length=100, blank=False)
#     dhcp = models.BooleanField(default=True)
#
#     def __unicode__(self):
#         return self.network
#
#
# class Router(models.Model):
#     project = models.ForeignKey(Project)
#     name = models.CharField(_('Router name'), max_length=100, blank=False)
#     internal_ip = models.CharField(_('Data center internal IP address'), max_length=100, blank=False)
#     external_ip = models.CharField(_('Valid IP address'), max_length=100, null=True)
#
#     def __unicode__(self):
#         return self.name
#
#
# class Port(models.Model):
#     router = models.ForeignKey(Router)
#     network = models.ForeignKey(Network)
#     ip = models.CharField(_('port IP address'), max_length=100, blank=False)
#
#     def __unicode__(self):
#         return self.name
#

class InfrastructureType(models.Model):
    class Meta:
        verbose_name = _('Infrastructure Type')
        verbose_name_plural = _('Infrastructure Types')

    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class InfrastructureRole(models.Model):
    class Meta:
        verbose_name = _('Infrastructure Role')
        verbose_name_plural = _('Infrastructure Roles')

    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Infrastructure(models.Model):
    data_center_code = models.CharField(max_length=100, blank=True, null=True)
    hostname = models.CharField(max_length=100, blank=False)
    role = models.ForeignKey(InfrastructureRole)
    type = models.ForeignKey(InfrastructureType)
    ram = models.CharField(max_length=100, blank=False)
    cpu = models.CharField(max_length=100, blank=False)
    hdd = models.CharField(max_length=100, blank=False)
    hdd_raid = models.CharField(max_length=100, blank=False, choices=RAID_CHOICES, default="raid5")
    operating_system = models.CharField(max_length=100, blank=False, default="Debian Wheezy")
    nic_count = models.CharField(max_length=100, blank=False)
    rack_number = models.CharField(max_length=100, blank=False)
    rack_u_number = models.CharField(max_length=100, blank=False)
    guarantee = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.hostname


class Nic(models.Model):
    infrastructure = models.ForeignKey(Infrastructure)
    name = models.CharField(max_length=100, null=True, blank=True, help_text=_("for example eth0, eth1, ..."))
    mac = models.CharField(max_length=100, blank=False)
    vlan = models.CharField(max_length=100, null=True, blank=True, choices=VLAN_CHOICES, default="vlan90")
    switch_port = models.CharField(max_length=100, null=True, blank=True)
    internal_ip = models.CharField(max_length=100, blank=False)
    external_ip = models.CharField(max_length=100, null=True, blank=True)
    firewall_access_rules = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return self.internal_ip


# class Instance(models.Model):
#     project = models.ForeignKey(Project)
#     machine = models.ForeignKey(Infrastructure)
#     name = models.CharField(max_length=100, blank=False)
#     ram = models.CharField(max_length=100, blank=True, null=True)
#     hdd = models.CharField(max_length=100, blank=True, null=True)
#     cpu = models.CharField(max_length=100, blank=True, null=True)
#     flavor = models.CharField(max_length=100, blank=True, null=True)
#     glance_image = models.CharField(max_length=100, blank=True, null=True)
#     hypervisor = models.CharField(max_length=100, blank=False, choices=HYPERVISOR_CHOICES, default="qemu")
#     gateway = models.ForeignKey(Router)
#     network = models.ForeignKey(Network)
#     openstack_internal_ip = models.CharField(_('Openstack internal IP address'), max_length=100, blank=False)
#     internal_ip = models.CharField(_('Datacenter internal IP address'), max_length=100, blank=False)
#     external_ip = models.CharField(_('Valid IP address'), max_length=100, blank=False)
#     datacenter_firewall = models.CharField(max_length=100, blank=True, null=True)
#     internal_firewall = models.CharField(max_length=100, blank=True, null=True, default="default")
#     description = models.TextField(blank=True, null=True)
#
#     def __unicode__(self):
#         return self.name

