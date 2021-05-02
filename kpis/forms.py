from django.forms import ModelForm
from .models import Brf, BrfKpi

class BrfForm(ModelForm):
    class Meta:
        model = Brf
        fields = ('name', 'founding_year')

class BrfKpiForm(ModelForm):
    class Meta:
        model = BrfKpi
        fields = ('brf','fiscal_year','interest_cost',
        	'net_sales','repairs','routine_maintenance',
        	'depreciation','result','net_debt')
