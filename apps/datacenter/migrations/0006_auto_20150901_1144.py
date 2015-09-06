# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0005_auto_20150901_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='computes_node_count',
            new_name='compute_node_count',
        ),
    ]
