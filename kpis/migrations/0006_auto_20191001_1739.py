# Generated by Django 2.2.4 on 2019-10-01 17:39

from django.db import migrations, models
import kpis.utils


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0005_auto_20190924_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='brfkpi',
            name='debt_kpi',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='brfkpi',
            name='interest_cost_kpi',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='brfkpi',
            name='uh_am_kpi',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='brfkpi',
            name='fiscal_year',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='brfkpi',
            name='net_sales',
            field=models.PositiveIntegerField(default=1, validators=[kpis.utils.validate_nonzero]),
        ),
    ]
