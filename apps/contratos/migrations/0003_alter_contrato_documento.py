# Generated by Django 4.0.8 on 2024-11-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='documento',
            field=models.FileField(upload_to='contratos'),
        ),
    ]