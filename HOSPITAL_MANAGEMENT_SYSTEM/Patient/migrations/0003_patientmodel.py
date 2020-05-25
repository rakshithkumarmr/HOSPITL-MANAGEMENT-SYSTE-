# Generated by Django 3.0.2 on 2020-05-24 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_auto_20200524_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=4)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.UserModel')),
            ],
        ),
    ]
