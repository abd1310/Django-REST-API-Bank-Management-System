# Generated by Django 4.2.16 on 2024-10-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_bankaccount_updated_at_alter_bankaccount_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.CharField(max_length=20),
        ),
    ]
