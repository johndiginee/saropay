# Generated by Django 4.2.2 on 2023-08-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_creditcard_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='number',
            field=models.CharField(max_length=20),
        ),
    ]