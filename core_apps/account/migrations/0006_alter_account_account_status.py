# Generated by Django 4.2.2 on 2023-07-17 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_kyc_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_status',
            field=models.CharField(choices=[('active', 'Active'), ('pending', 'Pending'), ('in-active', 'In-active')], default='in-active', max_length=100),
        ),
    ]
