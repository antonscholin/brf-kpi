from plotly.offline import plot
import plotly.graph_objects as go
import numpy as np

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('Quantity %(value)s is not allowed'),
            params={'value': value},
        )

def get_interest_cost_kpi(interest_cost, net_sales):
	# <15% : good
	# New BRFs can have up to 30%
	# If >30% : not good
	return interest_cost/net_sales

def get_uh_am_kpi(repairs, routine_maintenance, depreciation, result, net_sales):
	# >30% : good
	# new or debt free BRFs can have >15%
	# <0 : very bad!
	return (repairs + routine_maintenance + depreciation + result) / net_sales

def get_debt_kpi(net_debt, net_sales):
	# <5 : good
	# >10 : not good
	# >20 : very bad!
	return net_debt/net_sales

def get_plot_bg_shapes(bad_interval, medium_interval, good_interval, xmax, xmin):
	plot_bg_shapes = [
			go.layout.Shape(
	            type="rect",
	            layer="below",
	            x0=xmin,
	            y0=good_interval[0],
	            x1=xmax,
	            y1=good_interval[1],
	            line=dict(
	                width=0,
	            ),
	            fillcolor="#d6ffcc",
	        ),
	        go.layout.Shape(
	            type="rect",
	            layer="below",
	            x0=xmin,
	            y0=medium_interval[0],
	            x1=xmax,
	            y1=medium_interval[1],
	            line=dict(
	                width=0,
	            ),
	            fillcolor="#feffd1",
	        ),
	        go.layout.Shape(
	            type="rect",
	            layer="below",
	            x0=xmin,
	            y0=bad_interval[0],
	            x1=xmax,
	            y1=bad_interval[1],
	            line=dict(
	                width=0,
	            ),
	            fillcolor="#ffd6d6",
	        )]
	return plot_bg_shapes

def plot_interest_cost_kpi(Brf, BrfKpi):
	data = []
	xmax = 0
	xmin = 99000
	for brf_obj in Brf.objects.all():
		brf_kpi_objs = BrfKpi.objects.filter(brf=brf_obj)
		name = brf_obj.name
		years = []
		kpis = []
		for brf_kpi_obj in brf_kpi_objs:
			years.append(brf_kpi_obj.fiscal_year)
			kpis.append(brf_kpi_obj.interest_cost_kpi)
		trace = go.Scatter(
			x = years,
			y = kpis,
			name = name,
			mode = 'lines+markers',
			opacity = 0.8,
			visible = True)
		data.append(trace)
	
		# set x-values for background colors
		if years:
			if max(years)>xmax:
				xmax=max(years)

			if min(years)<xmin:
				xmin=min(years)

	# set y-values for background colors
	good_interval = [0,0.15]
	medium_interval = [0.15,0.3]
	bad_interval = [0.3,1]

	layout = dict(
		title="Räntekostnader",
		shapes = get_plot_bg_shapes(good_interval=good_interval, 
			medium_interval=medium_interval,
			bad_interval=bad_interval,
			xmax=xmax,
			xmin=xmin),
		yaxis=dict(
			rangemode='tozero')
	)
	
	# Create plotly figure
	fig = dict(data=data, layout=layout)
	# Get html and js to return
	plot_data = plot(fig, validate=False, show_link=False,config={'displayModeBar':False}, output_type='div')

	return plot_data

def plot_uh_am_kpi(Brf, BrfKpi):
	data = []
	xmax = 0
	xmin = 99000
	for brf_obj in Brf.objects.all():
		brf_kpi_objs = BrfKpi.objects.filter(brf=brf_obj)
		name = brf_obj.name
		years = []
		kpis = []
		for brf_kpi_obj in brf_kpi_objs:
			years.append(brf_kpi_obj.fiscal_year)
			kpis.append(brf_kpi_obj.uh_am_kpi)
		trace = go.Scatter(
			x = years,
			y = kpis,
			name = name,
			mode = 'lines+markers',
			opacity = 0.8,
			visible = True)
		data.append(trace)

		# set x-values for background colors
		if years:
			if max(years)>xmax:
				xmax=max(years)

			if min(years)<xmin:
				xmin=min(years)

	# set y-values for background colors
	bad_interval = [-0.5, 0.15]
	medium_interval = [0.15, 0.3]
	good_interval = [0.3, 1]
		
	layout = dict(
		title="UH/AM-utrymme",
		shapes = get_plot_bg_shapes(good_interval=good_interval, 
			medium_interval=medium_interval,
			bad_interval=bad_interval,
			xmax=xmax,
			xmin=xmin),
		yaxis=dict(
			rangemode='tozero')
	)
	
	# Create plotly figure
	fig = dict(data=data, layout=layout)
	# Get html and js to return
	plot_data = plot(fig, validate=False, show_link=False,config={'displayModeBar':False}, output_type='div')

	return plot_data

def plot_debt_kpi(Brf, BrfKpi):
	data = []
	xmax = 0
	xmin = 99000
	for brf_obj in Brf.objects.all():
		brf_kpi_objs = BrfKpi.objects.filter(brf=brf_obj)
		name = brf_obj.name
		years = []
		kpis = []
		for brf_kpi_obj in brf_kpi_objs:
			years.append(brf_kpi_obj.fiscal_year)
			kpis.append(brf_kpi_obj.debt_kpi)
		trace = go.Scatter(
			x = years,
			y = kpis,
			name = name,
			mode = 'lines+markers',
			opacity = 0.8,
			visible = True)
		data.append(trace)

		# set x-values for background colors
		if years:
			if max(years)>xmax:
				xmax=max(years)

			if min(years)<xmin:
				xmin=min(years)

	# set y-values for background colors
	bad_interval = [10, 30]
	medium_interval = [5, 10]
	good_interval = [0, 5]
		
	layout = dict(
		title="Skuldsättning",
		shapes = get_plot_bg_shapes(good_interval=good_interval, 
			medium_interval=medium_interval,
			bad_interval=bad_interval,
			xmax=xmax,
			xmin=xmin),
		yaxis=dict(
			rangemode='tozero')
	)
	
	# Create plotly figure
	fig = dict(data=data, layout=layout)
	# Get html and js to return
	plot_data = plot(fig, validate=False, show_link=False,config={'displayModeBar':False}, output_type='div')

	return plot_data
