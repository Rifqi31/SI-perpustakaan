# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0005_auto_20160814_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata_karyawan',
            name='foto',
            field=models.ImageField(blank=True, upload_to='/home/rifqi/mydjango/SI_perpustakaan/mystatic/media_root/upload'),
        ),
    ]