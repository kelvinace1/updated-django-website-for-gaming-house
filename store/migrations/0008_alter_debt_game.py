# Generated by Django 3.2.5 on 2021-12-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_debt_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='game',
            field=models.CharField(choices=[('ps4', 'ps4'), ('ps2', 'ps2'), ('ps3', 'ps3')], max_length=200, null=True),
        ),
    ]
