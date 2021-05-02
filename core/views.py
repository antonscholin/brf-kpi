from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'is_home': True})
