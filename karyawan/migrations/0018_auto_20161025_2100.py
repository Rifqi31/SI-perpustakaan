# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0017_auto_20160914_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biodata_karyawan',
            old_name='foto',
            new_name='foto_karyawan',
        ),
    ]
