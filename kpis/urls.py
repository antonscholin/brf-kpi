from django.urls import path

import kpis.views

urlpatterns = [
	#path('',kpis.views.home),
	path('add-brf', kpis.views.add_brf, name='add-brf'),
	path('add-kpis', kpis.views.add_kpis, name='add-kpis'),
	path('update-kpis', kpis.views.update_kpis, name='update-kpis'),
	path('plot-kpis', kpis.views.plot_kpis, name='plot-kpis'),
]