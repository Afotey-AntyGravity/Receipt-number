# Generated by Django 3.1.3 on 2021-04-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20210421_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesreceipt',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
