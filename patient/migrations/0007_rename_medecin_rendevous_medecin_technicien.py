# Generated by Django 3.2.3 on 2022-06-01 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_rendevous'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rendevous',
            old_name='medecin',
            new_name='medecin_technicien',
        ),
    ]
