# Generated by Django 3.2.5 on 2021-07-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvApp', '0004_alter_employee_empsal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='empSal',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7),
        ),
    ]