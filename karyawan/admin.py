from django.contrib import admin
from karyawan.models import biodata_karyawan, data_transaksi_peminjaman, Akun_karyawan
from karyawan.models import Kehadiran_karyawan, Izin_karyawan

import datetime
# Register your models here.

class karyawan_Admin(admin.ModelAdmin):
	list_display = ['nama_karyawan','jenis_kelamin','tgl_lahir','alamat','no_telepon','email']
	list_filter = ['jenis_kelamin']
	search_fields = ['nama_karyawan','no_telepon','email']
	list_per_page = 15

admin.site.register(biodata_karyawan, karyawan_Admin)



class peminjaman_Admin(admin.ModelAdmin):
	list_display = ['nama_peminjam','judul_buku','tgl_buku_dipinjam','tgl_buku_dikembalikan','status']
	#list_filter = []
	search_fields = ['nama_peminjam','judul_buku']
	list_per_page = 15

	actions = ['setuju_dipinjam','tidak_dipinjam']

	def setuju_dipinjam(self, request, queryset):
		for pinjam in queryset:
			diff = pinjam.tgl_buku_dikembalikan - pinjam.tgl_buku_dipinjam
			base = pinjam.tgl_buku_dikembalikan
			numdays = diff.days + 1
			date_list = [base - datetime.timedelta(days = x)for x in range(0, numdays)]

			pinjam.status = True
			pinjam.save()


	setuju_dipinjam.short_description = "Setuju peminjaman yang dipilih"


	def tidak_dipinjam(self, request, queryset):
		queryset.update(status = False)

	tidak_dipinjam.short_description = "Batalkan peminjaman yang dipilih"


admin.site.register(data_transaksi_peminjaman, peminjaman_Admin)



class Akunkaryawan_Admin(admin.ModelAdmin):
	list_display = ['akun','karyawan']
	#list_filter = []
	search_fields = ['akun','karyawan']
	list_per_page = 15

admin.site.register(Akun_karyawan, Akunkaryawan_Admin)


class kehadiran_Admin(admin.ModelAdmin):
	list_display = ['karyawan','jenis_kehadiran','waktu']
	#list_filter = []
	search_fields = ['karyawan','jenis_kehadiran']
	list_per_page = 15

admin.site.register(Kehadiran_karyawan, kehadiran_Admin)


class izin_Admin(admin.ModelAdmin):
	list_display = ['karyawan','jenis_kehadiran','waktu_mulai','waktu_berhenti','alasan','disetujui']
	#list_filter = []
	search_fields = ['karyawan']
	list_per_page = 15

	actions = ['setuju_izin','batalkan_izin']

	def setuju_izin(self, request, queryset):
		for izin in queryset:
			diff = izin.waktu_berhenti - izin.waktu_mulai
			base = izin.waktu_berhenti
			numdays = diff.days + 1
			date_list = [base - datetime.timedelta(days = x)for x in range(0, numdays)]

			for date in date_list:
				print date
				kehadiran = Kehadiran_karyawan(
					
					karyawan = izin.karyawan,
					jenis_kehadiran = izin.jenis_kehadiran,
					waktu = date 
					
					)
				kehadiran.save()

			izin.disetujui = True
			izin.save()

	setuju_izin.short_description = "Terima pengajuan izin yang dipilih"

	def batalkan_izin(self, request, queryset):
		queryset.update(disetujui = False)

	batalkan_izin.short_description = "Batalkan pengajuan yang dipilih"
	

admin.site.register(Izin_karyawan, izin_Admin)