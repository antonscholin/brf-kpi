# Generated by Django 2.2.4 on 2019-08-08 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('founding_year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BrfKpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('interest_cost', models.IntegerField(default=0)),
                ('net_sales', models.IntegerField(default=0)),
                ('repairs', models.IntegerField(default=0)),
                ('routine_maintenance', models.IntegerField(default=0)),
                ('depreciation', models.IntegerField(default=0)),
                ('result', models.IntegerField(default=0)),
                ('net_debt', models.IntegerField(default=0)),
                ('brf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kpis.Brf')),
            ],
        ),
    ]
