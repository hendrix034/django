# Generated by Django 5.0.6 on 2024-07-05 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id_ride', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('en-route', 'En-Route'), ('pickup', 'Pickup'), ('dropoff', 'Dropoff')], max_length=10)),
                ('pickup_latitude', models.FloatField()),
                ('pickup_longitude', models.FloatField()),
                ('dropoff_latitude', models.FloatField()),
                ('dropoff_longitude', models.FloatField()),
                ('pickup_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('other', 'Other')], max_length=5)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RideEvent',
            fields=[
                ('id_ride_event', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='rides.ride')),
            ],
        ),
        migrations.AddField(
            model_name='ride',
            name='id_driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides_as_driver', to='rides.user'),
        ),
        migrations.AddField(
            model_name='ride',
            name='id_rider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides_as_rider', to='rides.user'),
        ),
    ]
