# Generated by Django 3.2.3 on 2022-06-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20220601_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='resultatConsultation',
            field=models.TextField(max_length=1000),
        ),
    ]
