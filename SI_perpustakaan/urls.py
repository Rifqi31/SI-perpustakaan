"""SI_perpustakaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

#app as view

from anggota import views as anggota_views
from karyawan import views as karyawan_views
from buku import views as buku_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls','jet')),
   
    #anggota

    url(r'^$', anggota_views.profil),
    url(r'^login/', anggota_views.login_view),
    url(r'^logout/', anggota_views.logout_view),
    url(r'^register_bio/', anggota_views.register_bio_view),
    url(r'^register_user/', anggota_views.register_user_view),
    url(r'^ganti_foto/',anggota_views.ganti_foto),
    url(r'^pinjam_buku/',anggota_views.peminjaman_buku),
    url(r'^daftar_pinjam_buku/',anggota_views.tampil_buku_dipinjam),

    
    #karyawan

    url(r'^login_karyawan/', karyawan_views.login_karyawan_view),    
    url(r'^logout_karyawan/', karyawan_views.logout_karyawan_view),    
    url(r'^profil_karyawan/', karyawan_views.profil_karyawan),    
    url(r'^daftar_hadir/$', karyawan_views.daftar_hadir_karyawan),
    url(r'^daftar_izin/', karyawan_views.daftar_izin_karyawan),
    url(r'^pengajuan_izin/', karyawan_views.pengajuan_izin_karyawan),
    url(r'^ganti_foto_karyawan/',karyawan_views.ganti_foto_karyawan),
    url(r'^daftar_hadir/grafik/(?P<bulan>\d+)/(?P<tahun>\d+)$',karyawan_views.tampil_grafik, name ='show_grafik'),
    url(r'^daftar_hadir/cetak/(?P<bulan>\d+)/(?P<tahun>\d+)$',karyawan_views.cetak_daftar_hadir, name ='show_pdf'),


    #Dashboard-karyawan
    url(r'^dashboard/',karyawan_views.dashboard),

    #buku

    url(r'^tampil_tabel/', buku_views.tampil_tabel,),   
    url(r'^daftar_buku/', buku_views.daftar_buku, name ='daftar_buku'),
    url(r'^daftar_peminjam/', buku_views.daftar_peminjam, name ='daftar_peminjam'),
    url(r'^daftar_suplier/', buku_views.daftar_suplier_buku, name ='suplier'),
    url(r'^daftar_penyumbang/', buku_views.daftar_penyumbang_buku, name ='penyumbang'),


    #daftar anggota
    url(r'^daftar_anggota/', karyawan_views.daftar_anggota),


    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)