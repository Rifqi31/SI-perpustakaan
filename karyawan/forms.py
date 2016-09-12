from django.forms import ModelForm
from django import forms

from karyawan.models import Izin_karyawan

class Izin_karyawan_form(ModelForm):
	class Meta:
		model = Izin_karyawan
		fields = ['jenis_kehadiran','waktu_mulai','waktu_berhenti','alasan']
		labels = {

			'jenis_kehadiran':'Jenis Izin',
			'waktu_mulai':'Waktu mulai',
			'waktu_berhenti':'Waktu berhenti',
			'alasan':'Alasan',
		}
		error_messages = {

			'jenis_kehadiran':{
				'required':'Anda harus memilih jenis izin'
			},
			'waktu_mulai':{
				'required':'Anda harus menentukan tanggal izin dimulai'
			},
			'waktu_berhenti':{
				'required':'Anda harus menentukan tanggal izin berhenti'
			},
			'alasan':{
				'required':'Alasan harus diisi agar dapat disetujuti'
			}
		}
		widget = {
			'alasan':forms.Textarea(attrs = {'col':60,'row':10})
		}