# Generated by Django 4.0.3 on 2022-05-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_apartment_apartment_alt_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='features',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(default=True, max_length=300),
        ),
    ]
