# Generated by Django 3.1.3 on 2021-04-21 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0006_remove_comanyinformation_image'),
        ('sales', '0006_reference_customer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reference',
            new_name='SalesReceipt',
        ),
    ]
