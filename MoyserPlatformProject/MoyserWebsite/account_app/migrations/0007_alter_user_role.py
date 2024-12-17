# Generated by Django 5.1.4 on 2024-12-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0006_remove_disabilityuser_address_disabilityuser_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('companion', 'Companion'), ('beneficiary', 'Beneficiary'), ('admin', 'Admin')], default='beneficiary', max_length=15),
        ),
    ]