# Generated by Django 4.2.5 on 2023-09-20 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_remove_flat_owner_remove_flat_owner_pure_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complainant',
            new_name='author',
        ),
    ]
