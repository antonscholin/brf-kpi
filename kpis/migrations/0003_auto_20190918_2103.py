# Generated by Django 2.2.4 on 2019-09-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpis', '0002_auto_20190918_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brf',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
