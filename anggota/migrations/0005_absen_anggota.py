# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-14 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anggota', '0004_auto_20160814_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='absen_anggota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_absen', models.CharField(choices=[('Masuk', 'masuk'), ('Keluar', 'keluar')], max_length=30)),
                ('waktu', models.DateField()),
                ('nama_anggota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anggota.biodata')),
            ],
        ),
    ]
