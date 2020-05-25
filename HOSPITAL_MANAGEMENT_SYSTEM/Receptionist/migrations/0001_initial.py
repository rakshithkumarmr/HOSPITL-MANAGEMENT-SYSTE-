# Generated by Django 3.0.2 on 2020-05-24 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0002_prescription'),
        ('Patient', '0004_auto_20200524_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.PatientModel')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.DoctorModel')),
            ],
        ),
    ]