# Generated by Django 2.2.6 on 2020-08-12 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('cancel', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imgUrl', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('imgUrl', models.CharField(max_length=255, null=True)),
                ('experiences', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Experience')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('beds', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('roomType', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
                ('lng', models.DecimalField(decimal_places=2, max_digits=6)),
                ('lat', models.DecimalField(decimal_places=2, max_digits=6)),
                ('maxGuests', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('details', models.CharField(max_length=500)),
                ('imgUrl', models.CharField(max_length=500)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('properties', models.ManyToManyField(related_name='properties', through='main.Booking', to='main.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='main.Rating')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='main.Property'),
        ),
        migrations.AddField(
            model_name='booking',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.Review'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='main.User'),
        ),
    ]
