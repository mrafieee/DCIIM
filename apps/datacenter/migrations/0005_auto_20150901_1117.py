# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0004_auto_20150901_0802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='date',
            new_name='backup_file',
        ),
    ]
