# Generated by Django 2.2.6 on 2020-08-19 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200819_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='details',
            new_name='tagline',
        ),
        migrations.AddField(
            model_name='property',
            name='info',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
