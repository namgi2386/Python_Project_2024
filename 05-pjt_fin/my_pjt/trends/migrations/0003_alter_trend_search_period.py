# Generated by Django 4.2.16 on 2024-10-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0002_alter_keyword_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='search_period',
            field=models.TextField(),
        ),
    ]
