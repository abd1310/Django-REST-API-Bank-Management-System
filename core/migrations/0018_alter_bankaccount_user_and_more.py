# Generated by Django 4.2.16 on 2024-10-16 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_user_id_user_unique_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank_account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='bankaccount',
            constraint=models.UniqueConstraint(fields=('user',), name='unique_user_account'),
        ),
    ]
