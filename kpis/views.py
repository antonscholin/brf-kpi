from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .forms import BrfForm, BrfKpiForm
from .models import Brf, BrfKpi
from .utils import *

# class BrfKpiListView(ListView):
# 	model = BrfKpi
# 	context_object_name = "brfs"

# class BrfKpiCreateView(CreateView):
# 	model = BrfKpi
# 	fields = ('brf','fiscal_year','interest_cost',
# 		'net_sales','repairs','routine_maintenance',
# 		'depreciation','result','net_debt')

# class BrfKpiUpdateView(UpdateView):
# 	model = BrfKpi
# 	fields = ('brf','fiscal_year','interest_cost',
# 		'net_sales','repairs','routine_maintenance',
# 		'depreciation','result','net_debt')


def add_brf(request):
	if request.method=='POST':
		form = BrfForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'forms.html', {'form': form, 'saved':True})
	else:
		form = BrfForm()

	return render(request, 'forms.html', {'form': form, 'saved':False})

def add_kpis(request):
	if request.method=='POST':
		form = BrfKpiForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'forms.html', {'form': form, 'saved':True})
	else:
		form = BrfKpiForm()

	return render(request, 'forms.html', {'form': form, 'saved':False})

def update_kpis(request):
	return render(request, 'update_kpis.html', {'brf_kpis':BrfKpi.objects.all()})

def plot_kpis(request):
	interest_costs_html = plot_interest_cost_kpi(Brf, BrfKpi)
	uh_am_html = plot_uh_am_kpi(Brf, BrfKpi)
	debt_html = plot_debt_kpi(Brf, BrfKpi)

	return render(request, 'plot_kpis.html', {'interest_costs_html':interest_costs_html,
		'uh_am_html':uh_am_html,
		'debt_html':debt_html})
