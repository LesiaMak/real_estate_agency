# Generated by Django 4.2.5 on 2023-09-19 09:34

from django.db import migrations

def load_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            owner_name=flat.owner,
            owner_phone_number=flat.owner_pure_phone,)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(load_owners),
    ]
