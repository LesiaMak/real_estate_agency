# Generated by Django 4.2.5 on 2023-09-20 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_alter_complaint_complain_flat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
