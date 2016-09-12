from django.contrib import admin
from anggota.models import biodata, transaksi_peminjaman, Akun_perpus


# Register your models here.

class biodata_Admin(admin.ModelAdmin):

	list_display = ['nama','jenis_kelamin','tgl_lahir','alamat','no_telepon','email','status']
	list_filter = ['status','jenis_kelamin']
	search_fields = ['nama','email','no_telepon']
	list_per_page = 15


admin.site.register(biodata, biodata_Admin)


class transaksi_peminjaman_Admin(admin.ModelAdmin):

	list_display = ['nama_peminjam','judul_buku']
	#list_filter = []
	search_fields = ['judul_buku']
	list_per_page = 15


admin.site.register(transaksi_peminjaman, transaksi_peminjaman_Admin)


class Akunperpus_Admin(admin.ModelAdmin):

	list_display = ['akun','anggota']
	#list_filter = []
	search_fields = ['akun','anggota']
	list_per_page = 15

admin.site.register(Akun_perpus, Akunperpus_Admin)
