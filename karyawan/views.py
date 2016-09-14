from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#models and forms
from karyawan.models import biodata_karyawan, Kehadiran_karyawan, Izin_karyawan, Akun_karyawan
from karyawan.forms import *

 
# Create your views here.

def login_karyawan_view(request):
	if request.POST:
		user = authenticate(username=request.POST['username'],password=request.POST['password'])

		if user is not None:
			if user.is_active:
				try:
					akun = Akun_karyawan.objects.get(akun=user.id)
					login(request, user)

					request.session['karyawan_id'] = akun.karyawan.id
					request.session['username'] = request.POST['username']

				except:
					messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administartor')
				return redirect('/profil_karyawan/')

			else:
				messages.add_message(request, messages.INFO, 'User belum terverifikasi')

		else:
			messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

	return render(request, 'login_karyawan.html')


def logout_karyawan_view(request):
	logout(request)
	return redirect('/login_karyawan/')



@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_hadir_karyawan(request):
	daftar_hadir = None

	if request.method == 'POST':
		bulan = request.POST['bulan']
		tahun = request.POST['tahun']
		daftar_hadir = Kehadiran_karyawan.objects.filter(waktu__year = tahun, waktu__month = bulan, karyawan__id = request.session['karyawan_id'])

	return render(request, 'daftar_hadir.html',{'daftar_hadir':daftar_hadir})


@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def pengajuan_izin_karyawan(request):
	if request.method == 'POST':
		form_data = request.POST
		form = Izin_karyawan_form(form_data)

		if form.is_valid():
			izin = Izin_karyawan(

				karyawan = biodata_karyawan.objects.get(id = request.session['karyawan_id']),
				jenis_kehadiran = request.POST['jenis_kehadiran'],
				waktu_mulai = request.POST['waktu_mulai'],
				waktu_berhenti = request.POST['waktu_berhenti'],
				alasan = request.POST['alasan'],
				disetujui = False

				)
			izin.save()
			return redirect('/profil_karyawan/')

	else:
		form = Izin_karyawan_form()

	return render(request, 'tambah_izin.html', {'form':form})


@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_izin_karyawan(request):
	daftar_izin = Izin_karyawan.objects.filter(karyawan__id = request.session['karyawan_id']).order_by('waktu_mulai')

	#pagination
	paginator = Paginator(daftar_izin, 5)
	page = request.GET.get('page')
	try:
		daftar_izin = paginator.page(page)
	except PageNotAnInteger:
		daftar_izin = paginator.page(1)
	except EmptyPage:
		daftar_izin = paginator.page(paginator.num_pages)

	return render(request, 'daftar_izin.html',{'daftar_izin':daftar_izin})



@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def profil_karyawan(request):
	karyawan = biodata_karyawan.objects.get(id=request.session['karyawan_id'])

	return render(request, 'profil_karyawan.html',{'karyawan':karyawan})


@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def ganti_foto(request):
	karyawan = biodata_karyawan.objects.get(id=request.session['karyawan_id'])
	karyawan.foto = request.FILES['files']
	karyawan.save()

	return redirect('/profil_karyawan/')



#bahan pr belum selesai
@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def tampil_grafik(request, bulan, tahun):
	temp_char_data = []

	daftar_hadir = Kehadiran_karyawan.objects.filter(waktu__year = tahun, waktu__month = bulan, karyawan__id = request.session['karyawan_id'])

	temp_char_data.append({"x":"hadir","a":daftar_hadir.filter(jenis_kehadiran = 'hadir').count()})
	temp_char_data.append({"x":"izin","a":daftar_hadir.filter(jenis_kehadiran = 'izin').count()})
	temp_char_data.append({"x":"alpa","a":daftar_hadir.filter(jenis_kehadiran = 'alpa').count()})
	temp_char_data.append({"x":"cuti","a":daftar_hadir.filter(jenis_kehadiran = 'cuti').count()})

	chart_data = json.dumps({"data":temp_char_data})

	return render(request,'tampil_grafik.html',{'chart_data':chart_data,'bulan':bulan,'tahun':tahun})
