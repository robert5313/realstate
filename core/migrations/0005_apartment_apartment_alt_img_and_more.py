# Generated by Django 4.0.3 on 2022-05-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_apartment_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='apartment_alt_img',
            field=models.ImageField(default='default.jpg', upload_to='apartments/'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='apartment_img_2',
            field=models.ImageField(default='default.jpg', upload_to='apartments/'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='apartment_main_img',
            field=models.ImageField(default='default.jpg', upload_to='apartments/'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_alt_img',
            field=models.ImageField(default='default.jpg', upload_to='properties/'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_img_2',
            field=models.ImageField(default='default.jpg', upload_to='properties/'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_main_img',
            field=models.ImageField(default='default.jpg', upload_to='properties/'),
        ),
    ]
