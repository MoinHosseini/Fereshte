# Generated by Django 4.2.7 on 2023-12-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_item_availablity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
