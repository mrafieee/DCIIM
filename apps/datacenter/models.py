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
    ('raid1+ceph', 'RAID 1 + ceph'),
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
GROUP_CHOICES = (
    ('OX', 'OX'),
    ('NeX', 'NeX'),
    ('DeX', 'DeX'),
    ('Kerman', 'Kerman'),
)

CHANGES_TYPE_CHOICES = (
    ('Intallation', 'Intallation'),
    ('Openstack upgrade', 'Openstack upgrade'),
    ('Openstack new component', 'Openstack new component'),
    ('OS upgrade', 'OS upgrade'),
    ('Security upgrade', 'Security upgrade'),
    ('Other', 'Other'),
)

STATE_CHOICES = (
    ('Operational', 'Operational'),
    ("Under maintenance", 'Under maintenance'),
    ('Damaged', 'Damaged'),
    ('Not Configured', 'Not Configured'),
)

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
    group = models.CharField(max_length=100, blank=False, choices=GROUP_CHOICES, default="OX")
    state = models.CharField(max_length=100, blank=False, choices=STATE_CHOICES, default="Operational")
    ram = models.CharField(max_length=100, blank=False)
    cpu = models.CharField(max_length=100, blank=False)
    hdd = models.CharField(max_length=100, blank=False)
    hdd_raid = models.CharField(max_length=100, blank=False, choices=RAID_CHOICES, default="raid5")
    operating_system = models.CharField(max_length=100, blank=False, default="Debian Wheezy")
    nic_count = models.CharField(max_length=100, blank=False)
    datacenter_name = models.CharField(max_length=100, default="ITRC Datacenter", blank=False)
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

class Changes(models.Model):
    infrastructure = models.ForeignKey(Infrastructure)
    date = models.DateTimeField(default=datetime.now())
    type = models.CharField(max_length=100, blank=False,choices=CHANGES_TYPE_CHOICES, default='Openstack upgrade')
    description = models.TextField(blank=True, null=True)


class History(models.Model):
    class Meta:
        verbose_name_plural = _('History')

    backup_file = models.CharField(max_length=100, null=True, blank=True)
    instance_count = models.CharField(max_length=100, null=True, blank=True)
    projects_count = models.CharField(max_length=100, null=True, blank=True)
    floating_ips_count = models.CharField(max_length=100, null=True, blank=True)
    images_count = models.CharField(max_length=100, null=True, blank=True)
    compute_node_count = models.CharField(max_length=100, null=True, blank=True)
    controller_node_count = models.CharField(max_length=100, null=True, blank=True)
    network_node_count = models.CharField(max_length=100, null=True, blank=True)
    network_count = models.CharField(max_length=100, null=True, blank=True)
    routers_count = models.CharField(max_length=100, null=True, blank=True)
    #resources = models.CharField(max_length=100, null=True, blank=True)
    total_vcpu = models.CharField(max_length=100, null=True, blank=True)
    total_memory = models.CharField(max_length=100, null=True, blank=True)
    total_local_disk =models.CharField(max_length=100, null=True, blank=True)
    vcpu_used = models.CharField(max_length=100, null=True, blank=True)
    memory_used = models.CharField(max_length=100, null=True, blank=True)
    local_disk_used = models.CharField(max_length=100, null=True, blank=True)

