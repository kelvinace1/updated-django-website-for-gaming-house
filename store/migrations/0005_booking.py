# Generated by Django 3.2.5 on 2021-12-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('console', models.CharField(choices=[('1', 'ps1'), ('2', 'ps2'), ('3', 'ps3'), ('4', 'ps4')], max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]