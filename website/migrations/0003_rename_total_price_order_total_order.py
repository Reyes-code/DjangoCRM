# Generated by Django 5.0.4 on 2024-05-17 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_order_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_price',
            new_name='total_order',
        ),
    ]
