# Generated by Django 3.0.2 on 2020-05-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='usertype',
            field=models.CharField(max_length=8),
        ),
    ]
