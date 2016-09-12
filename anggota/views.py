from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.contrib.auth.models import User

#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from anggota.models import biodata
from anggota.forms import anggota_form, akun_form, peminjaman_form
from karyawan.models import data_transaksi_peminjaman
#from anggota.models import akun_anggota_form

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
	anggota = biodata.objects.get(id=request.session['anggota_id'])

	return render(request,'profil.html', {'anggota':anggota})


@login_required(login_url=settings.LOGIN_URL)
def ganti_foto(request):
	anggota = biodata.objects.get(id=request.session['anggota_id'])
	anggota.foto_anggota = request.FILES['files']
	anggota.save()

	return redirect('/')


@login_required(login_url=settings.LOGIN_URL)
def peminjaman_buku(request):
	if request.method == 'POST':
		form_data = request.POST
		form = peminjaman_form(form_data)

		if form.is_valid():
			pinjam = pinjam_buku(

				anggota = biodata.objects.get(id = request.session['anggota_id']),
				judul_buku = request.POST['judul_buku'],

				)
			pinjam.save()
			return redirect('/')

	else:
		form = peminjaman_form()

	return render(request,'form_peminjaman.html',{'form':form})


@login_required(login_url = settings.LOGIN_URL)
def tampil_buku_dipinjam(request):

	daftar_buku_dipinjam = data_transaksi_peminjaman.objects.filter(id = request.session['anggota_id'])

	#pagination
	paginator = Paginator(daftar_buku_dipinjam, 5)
	page = request.GET.get('page')

	try:
		daftar_buku_dipinjam = paginator.page(page)
	except PageNotAnInteger:
		daftar_buku_dipinjam = paginator.page(1)
	except EmptyPage:
		daftar_buku_dipinjam = paginator.page(paginator.num_pages)

	return render(request,'daftar_buku_dipinjam.html',{'daftar_buku_dipinjam':daftar_buku_dipinjam})


def register_bio_view(request):
	if request.method == 'POST':
		form_data = request.POST
		form = anggota_form(form_data)

		if form.is_valid():
			bio = biodata(

				nama = request.POST['nama'],
				jenis_kelamin = request.POST['jenis_kelamin'],
				tgl_lahir = request.POST['tgl_lahir'],
				alamat = request.POST['alamat'],
				no_telepon = request.POST['no_telepon'],
				email = request.POST['email'],
				status = request.POST['status'],
				
				)
			bio.save()

			return redirect('/login/')
	else:
		form = anggota_form()

	return render(request, 'register_bio.html',{'form':form})


def register_user_view(request):
	if request.method == 'POST':
		form_data = request.POST
		form = akun_form(form_data)

		if form.is_valid():

			new_user = User.objects.create_user(**form.cleaned_data)


			return redirect('/register_bio/')
	else:
		form = akun_form()

	return render(request, 'register_bio.html',{'form':form})