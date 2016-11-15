from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.http import HttpResponse

#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Reportlab
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors

#models and forms
from karyawan.models import biodata_karyawan, Kehadiran_karyawan, Izin_karyawan, Akun_karyawan, data_transaksi_peminjaman
from karyawan.forms import *
from anggota.models import biodata


from django.utils import timezone

import json, time

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



@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def absen_karyawan(request):
	karyawan = Kehadiran_karyawan.objects.get(id = request.session['karyawan_id']),
	jenis_kehadiran = Kehadiran_karyawan.objects.get(jenis_kehadiran = 'hadir'),
	waktu = timezone.now()



@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def ganti_foto_karyawan(request):
	karyawan = biodata_karyawan.objects.get(id=request.session['karyawan_id'])
	karyawan.foto_karyawan = request.FILES['files']
	karyawan.save()

	return redirect('/profil_karyawan/')


@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_hadir_karyawan(request):
	daftar_hadir = None

	bulan = 0
	tahun = 0

	if request.method == 'POST':
		bulan = request.POST['bulan']
		tahun = request.POST['tahun']
		daftar_hadir = Kehadiran_karyawan.objects.filter(waktu__year = tahun, waktu__month = bulan, karyawan__id = request.session['karyawan_id'])

	return render(request, 'daftar_hadir.html',{'daftar_hadir':daftar_hadir, 'bulan':bulan, 'tahun':tahun})


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


@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def ganti_foto(request):
	karyawan = biodata_karyawan.objects.get(id=request.session['karyawan_id'])
	karyawan.foto = request.FILES['files']
	karyawan.save()

	return redirect('/profil_karyawan/')




@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def tampil_grafik(request, bulan, tahun):
	temp_chart_data = []

	daftar_hadir = Kehadiran_karyawan.objects.filter(waktu__year=tahun, waktu__month=bulan, karyawan__id=request.session['karyawan_id'])

	temp_chart_data.append({"x":"hadir","a":daftar_hadir.filter(jenis_kehadiran='hadir').count() })
	temp_chart_data.append({"x":"izin","a":daftar_hadir.filter(jenis_kehadiran='izin').count() })
	temp_chart_data.append({"x":"alpa","a":daftar_hadir.filter(jenis_kehadiran='alpa').count() })
	temp_chart_data.append({"x":"cuti","a":daftar_hadir.filter(jenis_kehadiran='cuti').count() })

	chart_data = json.dumps({"data":temp_chart_data})

	return render(request, 'tampil_grafik.html',{'chart_data':chart_data, 'bulan':bulan, 'tahun':tahun})



@login_required(login_url=settings.LOGIN_KARYAWAN_URL)
def cetak_daftar_hadir(request, bulan, tahun):
	#pengaturan respon berformat pdf
	filename = "daftar_hadir_" + str(bulan) + "_" + str(tahun)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment;filename="' + filename + '.pdf"'

	#mengambil daftar kehadiran dan mengubahnya menjadi data untuk tabel
	data = Kehadiran_karyawan.objects.filter(waktu__year=tahun, waktu__month=bulan, karyawan__id=request.session['karyawan_id'])
	#data = Kehadiran_karyawan.objects.filter(karyawan__id=request.session['karyawan_id'])
	
	table_data = []
	table_data.append(["Tanggal","Status"])
	for x in data:
		table_data.append([ x.waktu, x.jenis_kehadiran ])

	#membuat dokumen baru
	doc = SimpleDocTemplate(response, pagesizes=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
	styles = getSampleStyleSheet()

	#pengaturan tabel di pdf
	table_style = TableStyle([
					('ALIGN',(1,1),(-2,-2),'RIGHT'),
					('FONT',(0,0),(-1,0),'Helvetica-Bold'),
					('VALIGN',(0,0),(0,-1),'TOP'),
					('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
					('BOX',(0,0),(-1,-1),0.25,colors.black),
		])
	kehadiran_table= Table(table_data, colWidths=[doc.width/4.0]*2)
	kehadiran_table.setStyle(table_style)

	#mengisi pdf
	content = []
	content.append(Paragraph('Daftar Kehadiran %s%s' % (bulan, tahun), styles['Title']))
	content.append(Spacer(1,12))
	content.append(Paragraph('Berikut ini adalah hasil rekam jejak kehadiran Anda selama bulan %s tahun %s:' % (bulan, tahun), styles['Normal']))
	content.append(Spacer(1,12))
	content.append(kehadiran_table)
	content.append(Spacer(1,36))
	content.append(Paragraph('Mengetahui,',styles['Normal']))
	content.append(Spacer(1,48))
	content.append(Paragraph('Rifqi Muttaqin, Head of Departement PT.iDEA Development.',styles['Normal']))

	#menghasilkan pdf untuk di download
	doc.build(content)
	return response



#daftar anggota
@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def daftar_anggota(request):
	#data anggota

	data_anggota = biodata.objects.all()

	#pagination
	paginator = Paginator(data_anggota, 5)
	page = request.GET.get('page')
	try:
		data_anggota = paginator.page(page)
	except PageNotAnInteger:
		data_anggota = paginator.page(1)
	except EmptyPage:
		data_anggota= paginator.page(paginator.num_pages)


	return render(request, 'daftar_anggota.html',{'data_anggota':data_anggota})


#dashboard
@login_required(login_url = settings.LOGIN_KARYAWAN_URL)
def dashboard(request):


	#data grafik anggota

	temp_chart_data = []

	grafik_jenis_anggota = biodata.objects.all()

	temp_chart_data.append({"x":"bekerja","a":grafik_jenis_anggota.filter(status='bekerja').count() })
	temp_chart_data.append({"x":"pelajar","a":grafik_jenis_anggota.filter(status='pelajar').count() })
	temp_chart_data.append({"x":"mahasiswa","a":grafik_jenis_anggota.filter(status='mahasiswa').count() })
	temp_chart_data.append({"x":"umum","a":grafik_jenis_anggota.filter(status='umum').count() })

	chart_data = json.dumps({"data":temp_chart_data})



	return render(request,'dashboard.html',{'chart_data':chart_data})