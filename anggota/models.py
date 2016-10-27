from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class biodata(models.Model):

	JENIS_KELAMIN_CHOICE = {

		('Pria','pria'),
		('Wanita','wanita')
	}

	PILIH_STATUS_CHOICE = {

		('Bekerja','bekerja'),
		('Pelajar','pelajar'),
		('Mahasiswa','mahasiswa'),
		('Umum','umum')
	}

	nama = models.CharField(max_length = 100)
	jenis_kelamin = models.CharField(max_length = 15, choices = JENIS_KELAMIN_CHOICE)
	tgl_lahir = models.DateField()
	alamat = models.TextField()
	no_telepon = models.CharField(max_length=12)
	email = models.EmailField()
	status = models.CharField(max_length = 50, choices = PILIH_STATUS_CHOICE)
	foto_anggota = models.ImageField(upload_to = "upload", null = True)


	def __unicode__(self):
		return self.nama


class transaksi_peminjaman(models.Model):


	nama_peminjam = models.ForeignKey(biodata)
	judul_buku = models.CharField(max_length = 100)


	def __unicode__(self):
		return self.nama_peminjam.nama


class Akun_perpus(models.Model):

	akun = models.ForeignKey(User)
	anggota = models.ForeignKey(biodata)

	def __unicode__(self):
		return self.anggota.nama


class kehadiran_anggota(models.Model):

	JENIS_ABSEN_CHOICE = {

		('masuk','Masuk'),
		('keluar','Keluar')
	}

	anggota = models.ForeignKey(biodata)
	jenis_absen = models.CharField(max_length = 6, choices = JENIS_ABSEN_CHOICE)
	waktu = models.DateTimeField()

	def __unicode__(self):
		return anggota.nama