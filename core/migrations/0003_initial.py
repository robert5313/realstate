# Generated by Django 4.0.3 on 2022-03-18 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_delete_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(max_length=50)),
                ('rent_price', models.IntegerField()),
                ('features', models.TextField(default=True, max_length=100)),
                ('floor_number', models.IntegerField()),
                ('rent_payment_status', models.BooleanField()),
                ('occupant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tenant.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='RentIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date_received', models.DateTimeField(auto_now=True)),
                ('apartment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.apartment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'A property with that name already exists.'}, max_length=50, unique=True)),
                ('address', models.TextField(default='', max_length=100)),
                ('type', models.CharField(choices=[('1', 'Bedistters'), ('2', 'Bedistters, 1 bedroom or more Apartments'), ('3', 'Studio Apartments, bedsitters, 1 bedroom or more Apartments')], max_length=50)),
                ('floor', models.IntegerField()),
                ('county', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('description', models.TextField(default=True, max_length=100)),
                ('account_number', models.IntegerField()),
                ('rent_till_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('purpose', models.TextField(default='')),
                ('date_incurred', models.DateTimeField(auto_now=True)),
                ('apartment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.apartment')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.property'),
        ),
    ]
