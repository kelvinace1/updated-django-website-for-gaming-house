# Generated by Django 3.2.5 on 2021-12-15 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]