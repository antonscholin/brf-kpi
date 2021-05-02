from django.db import models
from .utils import get_interest_cost_kpi, validate_nonzero, get_uh_am_kpi, get_debt_kpi

class Brf(models.Model):
    name = models.CharField(max_length=200, unique=True)
    founding_year = models.IntegerField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    #address = 

class BrfKpi(models.Model):
    brf = models.ForeignKey(Brf, on_delete=models.CASCADE)
    fiscal_year = models.PositiveIntegerField(blank=False)
    interest_cost = models.IntegerField(default=0)
    net_sales = models.PositiveIntegerField(default=1,
        validators=[validate_nonzero])
    repairs = models.IntegerField(default=0)
    routine_maintenance = models.IntegerField(default=0)
    depreciation = models.IntegerField(default=0)
    result = models.IntegerField(default=0)
    net_debt = models.IntegerField(default=0)
    interest_cost_kpi = models.FloatField(default=0)
    uh_am_kpi = models.FloatField(default=0)
    debt_kpi = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.interest_cost_kpi = get_interest_cost_kpi(
            self.interest_cost,
            self.net_sales)
        self.uh_am_kpi = get_uh_am_kpi(
            self.repairs,
            self.routine_maintenance,
            self.depreciation,
            self.result,
            self.net_sales)
        self.debt_kpi = get_debt_kpi(
            self.net_debt,
            self.net_sales)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.brf)+', '+str(self.fiscal_year)

    class Meta:
        unique_together = (("brf", "fiscal_year"),)  

