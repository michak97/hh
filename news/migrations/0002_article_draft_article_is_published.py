# Generated by Django 5.1.2 on 2025-01-07 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
