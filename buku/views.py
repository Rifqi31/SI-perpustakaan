from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#models
from buku.models import *
from karyawan.models import data_transaksi_peminjaman

# Create your views here.

@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def tampil_tabel(request):

	#data buku

	daftar_buku = data_buku.objects.all()

	#pagination
	paginator = Paginator(daftar_buku, 10)
	page = request.GET.get('page')
	try:
		daftar_buku = paginator.page(page)
	except PageNotAnInteger:
		daftar_buku = paginator.page(1)
	except EmptyPage:
		daftar_buku = paginator.page(paginator.num_pages)



	#daftar peminjam buku

	daftar_pinjam = data_transaksi_peminjaman.objects.all()

	#pagination
	paginator = Paginator(daftar_pinjam, 5)
	page = request.GET.get('page')
	try:
		daftar_pinjam = paginator.page(page)
	except PageNotAnInteger:
		daftar_pinjam = paginator.page(1)
	except EmptyPage:
		daftar_pinjam = paginator.page(paginator.num_pages)



	#data suplier

	daftar_suplier = suplier_buku.objects.all()

	#pagination
	pagination = Paginator(daftar_suplier, 5)
	page = request.GET.get('page')
	try:
		daftar_suplier = paginator.page(page)
	except PageNotAnInteger:
		daftar_suplier = paginator.page(1)
	except EmptyPage:
		daftar_suplier = paginator.page(paginator.num_pages)


	#data penyumbang

	daftar_penyumbang = penyumbang_buku.objects.all()

	#pagination
	pagination = Paginator(daftar_penyumbang, 5)
	page = request.GET.get('page')
	try:
		daftar_penyumbang = paginator.page(page)
	except PageNotAnInteger:
		daftar_penyumbang = paginator.page(1)
	except EmptyPage:
		daftar_penyumbang = paginator.page(paginator.num_pages)	

	return render(request, "tampil_tabel.html",{'daftar_buku':daftar_buku,'daftar_pinjam':daftar_pinjam,'daftar_suplier':daftar_suplier,'daftar_penyumbang':daftar_penyumbang})



@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_buku(request):
	daftar_buku = None

	if request.method == 'POST':
		jenis = request.POST['jenis_buku']

		daftar_buku = data_buku.objects.filter() 

		#pagination
		paginator = Paginator(daftar_buku, 10)
		page = request.GET.get('page')
		try:
			daftar_buku = paginator.page(page)
		except PageNotAnInteger:
			daftar_buku = paginator.page(1)
		except EmptyPage:
			daftar_buku = paginator.page(paginator.num_pages)


	return render(request, 'daftar_buku.html',{'daftar_buku':daftar_buku})


@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_peminjam(request):

	daftar_peminjam = None

	if request.method == 'POST':

		daftar_peminjam = data_transaksi_peminjaman.objects.filter(judul_buku = request.POST['judul_buku'])

	else:
		daftar_peminjam = data_transaksi_peminjaman.objects.all()


		#pagination
		paginator = Paginator(daftar_peminjam, 10)
		page = request.GET.get('page')
		try:
			daftar_peminjam = paginator.page(page)
		except PageNotAnInteger:
			daftar_peminjam = paginator.page(1)
		except EmptyPage:
			daftar_peminjam = paginator.page(paginator.num_pages)


	return render(request, 'daftar_peminjam.html',{'daftar_peminjam':daftar_peminjam})



@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_suplier_buku(request):

	daftar_suplier = suplier_buku.objects.all()

	#pagination
	paginator = Paginator(daftar_suplier, 10)
	page = request.GET.get('page')
	try:
		daftar_suplier = paginator.page(page)
	except PageNotAnInteger:
		daftar_suplier = paginator.page(1)
	except EmptyPage:
		daftar_suplier = paginator.page(paginator.num_pages)

	return render(request, 'daftar_suplier.html',{'daftar_suplier':daftar_suplier})


@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_penyumbang_buku(request):

	daftar_penyumbang = penyumbang_buku.objects.all()

	#pagination
	paginator = Paginator(daftar_penyumbang, 10)
	page = request.GET.get('page')
	try:
		daftar_penyumbang = paginator.page(page)
	except PageNotAnInteger:
		daftar_penyumbang = paginator.page(1)
	except EmptyPage:
		daftar_penyumbang = paginator.page(paginator.num_pages)

	return render(request, 'daftar_penyumbang.html',{'daftar_penyumbang':daftar_penyumbang})	