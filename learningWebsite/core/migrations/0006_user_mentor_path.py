# Generated by Django 4.0.5 on 2023-04-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_address_user_hour_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mentor_path',
            field=models.CharField(default='Python programavimas, IT saugumas', max_length=255),
        ),
    ]