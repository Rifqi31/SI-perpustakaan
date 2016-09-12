from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from anggota.models import biodata, Akun_perpus
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
	if request.POST:
		user = authenticate(username=request.POST['username'],password=request.POST['password'])

		if user is not None:
			if user.is_active:
				try:
					akun = Akun_perpus.objects.get(akun=user.id)
					login(request, user)

					request.session['anggota_id'] = akun.anggota.id
					request.session['username'] = request.POST['username']

				except:
					messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data anggota, silahkan hubungi administartor')
				return redirect('/')

			else:
				messages.add_message(request, messages.INFO, 'User belum terverifikasi')

		else:
			messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

	return render(request, 'login.html')


def logout_view(request):
	logout(request)
	return redirect('/login/')