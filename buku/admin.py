from django.contrib import admin
from buku.models import data_buku, suplier_buku, penyumbang_buku

# Register your models here.

class databuku_Admin(admin.ModelAdmin):
	list_display = ['judul_buku','jenis_buku','penulis','tgl_terbit','penerbit']
	list_filter = ['jenis_buku']
	search_fields = ['judul_buku','jenis_buku','penulis']
	list_per_page = 15

admin.site.register(data_buku, databuku_Admin)


class suplier_Admin(admin.ModelAdmin):
	list_display = ['nama_suplier','tgl_terima','alamat_suplier','judul_buku','jumlah_buku']
	#list_filter = []
	search_fields = ['nama_suplier']
	list_per_page = 15

admin.site.register(suplier_buku, suplier_Admin)


class penyumbang_Admin(admin.ModelAdmin):
	list_display = ['nama_penyumbang','tgl_terima','alamat_penyumbang','judul_buku','jumlah_buku']
	#list_filter = []
	search_fields = ['nama_penyumbag']
	list_per_page = 15

admin.site.register(penyumbang_buku, penyumbang_Admin) 