# Generated by Django 4.2 on 2023-04-18 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_user_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.group'),
        ),
    ]
