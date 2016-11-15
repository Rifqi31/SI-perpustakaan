from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

from anggota.models import biodata
from buku.models import data_buku

# Create your models here.

#Petugas
class biodata_karyawan(models.Model):

	JENIS_KELAMIN_CHOICE = {

		('Pria','pria'),
		('Wanita','wanita')
	}

	nama_karyawan = models.CharField(max_length = 100)
	jenis_kelamin = models.CharField(max_length = 15, choices = JENIS_KELAMIN_CHOICE)
	tgl_lahir = models.DateField()
	alamat = models.TextField()
	no_telepon = models.CharField(max_length=12)
	email = models.EmailField() 
	foto_karyawan = models.ImageField(upload_to = "upload")

	def __unicode__(self):
		return self.nama_karyawan


class data_transaksi_peminjaman(models.Model):

	nama_peminjam = models.ForeignKey(biodata)
	judul_buku = models.CharField(max_length = 100)
	tgl_buku_dipinjam = models.DateField(null = True)
	tgl_buku_dikembalikan = models.DateField(null = True)
	status = models.BooleanField(default = False)

	def __unicode__(self):
		return self.nama_peminjam.nama


class Akun_karyawan(models.Model):

	akun = models.ForeignKey(User)
	karyawan = models.ForeignKey(biodata_karyawan)

	def __unicode__(self):
		return self.karyawan.nama_karyawan


class Kehadiran_karyawan(models.Model):

	JENIS_KEHADIRAN_CHOICE = {

		('izin','Izin'),
		('cuti','Cuti'),
		('alpa','Tanpa Kehadiran'),
		('hadir','Hadir'),
	}

	karyawan = models.ForeignKey(biodata_karyawan)
	jenis_kehadiran = models.CharField(max_length = 50, choices = JENIS_KEHADIRAN_CHOICE)
	waktu = models.DateField()

	def absen(self):
		self.waktu = timezone.now()
		self.save()

	def __unicode__(self):
		return self.karyawan.nama_karyawan


class Izin_karyawan(models.Model):

	JENIS_KEHADIRAN_CHOICE = {

		('izin','Izin'),
		('cuti','Cuti'),
	}

	karyawan = models.ForeignKey(biodata_karyawan)
	jenis_kehadiran = models.CharField(max_length = 50, choices = JENIS_KEHADIRAN_CHOICE)
	waktu_mulai = models.DateField()
	waktu_berhenti = models.DateField()
	alasan = models.TextField()
	disetujui = models.BooleanField(default = False)

	def __unicode__(self):
		return self.karyawan.nama_karyawan
