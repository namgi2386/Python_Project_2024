# Generated by Django 4.2.11 on 2024-10-04 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]