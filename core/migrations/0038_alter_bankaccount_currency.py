# Generated by Django 4.2.16 on 2024-10-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_alter_bankaccount_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='currency',
            field=models.CharField(choices=[('NIS', 'New Israeli Shekel'), ('USD', 'US Dollar'), ('EUR', 'Euro')], default='NIS', max_length=3),
        ),
    ]
