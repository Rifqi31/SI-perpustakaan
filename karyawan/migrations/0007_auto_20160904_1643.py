# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0006_biodata_karyawan_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata_karyawan',
            name='foto',
            field=models.ImageField(upload_to='upload'),
        ),
    ]
