# Generated by Django 4.2.5 on 2023-09-19 09:41

from django.db import migrations

def load_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    for owner in owners.iterator():
        flats = Flat.objects.filter(owner=owner.owner_name)
        owner.have_flats.set(flats)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230919_1334'),
    ]

    operations = [
        migrations.RunPython(load_flats),
    ]
