# Generated by Django 4.2.16 on 2024-10-25 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_rename_original_currency_transaction_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='original_amount',
        ),
    ]