# Generated by Django 4.0.3 on 2022-05-17 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_customerrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerrequest',
            old_name='apartment_id',
            new_name='apartment',
        ),
    ]
