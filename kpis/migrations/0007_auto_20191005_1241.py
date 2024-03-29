# Generated by Django 2.2.4 on 2019-10-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0006_auto_20191001_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brfkpi',
            name='fiscal_year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='brfkpi',
            unique_together={('brf', 'fiscal_year')},
        ),
    ]
