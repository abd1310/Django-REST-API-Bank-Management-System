# Generated by Django 4.2.16 on 2024-10-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_bankaccount_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.CharField(max_length=20),
        ),
    ]
