# Generated by Django 3.1.3 on 2021-05-31 19:38

from django.db import migrations, models
import proforma.models


class Migration(migrations.Migration):

    dependencies = [
        ('proforma', '0002_auto_20210510_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proformareceipt',
            name='reference_Number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
