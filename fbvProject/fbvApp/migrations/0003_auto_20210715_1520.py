# Generated by Django 3.2.5 on 2021-07-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvApp', '0002_auto_20210715_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesalary',
            name='basic',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='employeesalary',
            name='status',
            field=models.BooleanField(),
        ),
    ]
