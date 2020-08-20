# Generated by Django 2.2.6 on 2020-08-19 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200818_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='property',
            name='imgUrl',
        ),
        migrations.AddField(
            model_name='gallery',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Property'),
        ),
        migrations.AddField(
            model_name='property',
            name='img',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='main.Review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='main.Rating'),
        ),
    ]
