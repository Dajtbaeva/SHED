# Generated by Django 4.2 on 2023-04-19 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_group_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organization'),
        ),
    ]
