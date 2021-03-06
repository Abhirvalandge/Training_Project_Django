# Generated by Django 3.2.5 on 2021-07-15 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fbvApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='empSal',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='employee',
            name='empStatus',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic', models.IntegerField()),
                ('hra', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('empId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbvApp.employee')),
            ],
        ),
    ]
