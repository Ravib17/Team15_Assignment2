# Generated by Django 3.1.1 on 2020-09-08 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product',
        ),
    ]
