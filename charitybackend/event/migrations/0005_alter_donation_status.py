# Generated by Django 4.1.4 on 2023-01-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_photo_alter_donation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]