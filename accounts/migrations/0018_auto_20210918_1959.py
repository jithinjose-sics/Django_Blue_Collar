# Generated by Django 3.2.6 on 2021-09-18 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_employee_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='adharno',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='zipcode',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]