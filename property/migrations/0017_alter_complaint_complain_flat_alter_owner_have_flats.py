# Generated by Django 4.2.5 on 2023-09-20 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_rename_owner_name_owner_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complain_flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.flat', verbose_name='Квартира, на которую жаловались'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='have_flats',
            field=models.ManyToManyField(db_index=True, related_name='owners', to='property.flat', verbose_name='Квартиры в собственности'),
        ),
    ]
