# Generated by Django 5.0.6 on 2024-06-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0002_command'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='favourite',
            field=models.CharField(default='False', max_length=255),
        ),
    ]
