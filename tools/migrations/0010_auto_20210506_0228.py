# Generated by Django 3.1.3 on 2021-05-06 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0009_discounttable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybankaccountinformation',
            name='account_Number',
            field=models.PositiveIntegerField(null=True),
        ),
    ]