from __future__ import unicode_literals

from django.db import models

# Create your models here.

class data_buku(models.Model):

	JENIS_BUKU_CHOICE = {

		('Novel','novel'),
		('Cerpen','Cerpen'),
		('Majalah','majalah'),
		('Komik','komik'),
		('Manga','manga'),
		('Komputer','komputer'),
		('Sekolah','sekolah')
	}

	judul_buku = models.CharField(max_length = 100)
	jenis_buku = models.CharField(max_length = 50, choices = JENIS_BUKU_CHOICE)
	penulis = models.CharField(max_length = 50)
	tgl_terbit = models.DateField()
	penerbit = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.judul_buku


class suplier_buku(models.Model):

	nama_suplier = models.CharField(max_length = 100)
	tgl_terima = models.DateField()
	alamat_suplier= models.TextField()
	judul_buku = models.CharField(max_length = 100)
	jumlah_buku = models.IntegerField()

	def __unicode__(self):
		self.nama_suplier


class penyumbang_buku(models.Model):

	nama_penyumbang = models.CharField(max_length = 100)
	tgl_terima = models.DateField()
	alamat_penyumbang= models.TextField()
	judul_buku = models.CharField(max_length = 100)
	jumlah_buku = models.IntegerField()

	def __unicode__(self):
		self.nama_penyumbang	
