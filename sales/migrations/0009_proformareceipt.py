# Generated by Django 3.1.3 on 2021-04-21 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0007_tax'),
        ('sales', '0008_salesreceipt_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProformaReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_Number', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('discount_Rate', models.FloatField(null=True)),
                ('unit_Price', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.currency')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.customer')),
                ('material_Color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.materialcolourinformation')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.product')),
                ('sales_Officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.salesmaninformation')),
            ],
        ),
    ]
