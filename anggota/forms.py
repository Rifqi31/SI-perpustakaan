from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from anggota.models import biodata
from anggota.models import transaksi_peminjaman
#from anggota.models import Akun_perpus


class anggota_form(ModelForm):
	class Meta:
		model = biodata
		fields = ['nama','jenis_kelamin','tgl_lahir','alamat','no_telepon','email','status']
		labels = {

			'nama':'Nama Lengkap',
			'jenis_kelamin':'Jenis Kelamin',
			'tgl_lahir':'Tanggal Lahir',
			'alamat':'Alamat',
			'no_telepon':'No Telepon',
			'email':'Email',
			'status':'status',

		}
		error_messages = {

			'nama':{
				'required':'Anda harus mengisi nama'
			},
			'jenis_kelamin':{
				'required':'Anda harus memilih jenis kelamin'
			},
			'tgl_lahir':{
				'required':'Anda harus mengisi tanggal lahir'
			},
			'alamat':{
				'required':'Anda harus mengisi alamat'
			},
			'no_telepon':{
				'required':'Anda harus mengisi nomer telepon'
			},
			'email':{
				'required':'Anda harus mengisi email'
			},
			'status':{
				'required':'Anda harus memilih status'
			}
		}
		widget = {
			'alamat':forms.Textarea(attrs={'col':50,'row':10})
		}


class akun_form(ModelForm):
	class Meta:
		model = User
		fields = ['username','password']



class peminjaman_form(ModelForm):
	class Meta:
		model = transaksi_peminjaman
		fields = ['judul_buku']
		labels = {

			'judul_buku':'Judul',
		}
		error_messages = {
			'judul_buku':{
				'required':'anda harus mengisi judul buku'
			},
		}