# Generated by Django 4.1.5 on 2023-01-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(blank=True, default=34),
            preserve_default=False,
        ),
    ]
