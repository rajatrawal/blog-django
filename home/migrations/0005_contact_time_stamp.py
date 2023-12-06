# Generated by Django 3.1.7 on 2021-03-18 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_contact_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]