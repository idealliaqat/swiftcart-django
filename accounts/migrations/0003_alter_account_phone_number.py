# Generated by Django 5.0.1 on 2024-03-09 22:18

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_date_joined2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Enter your 11-digit phone number with digits only.', max_length=128, region=None),
        ),
    ]