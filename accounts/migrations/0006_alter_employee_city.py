# Generated by Django 3.2.6 on 2021-08-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_employee_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(choices=[('', 'CITY'), ('TVM', 'TVM'), ('CALICUT', 'CALICUT'), ('KOCHIN', 'KOCHIN')], max_length=34, null=True),
        ),
    ]
