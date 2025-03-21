# Generated by Django 5.1.2 on 2025-01-13 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_alter_teaser_image_file_alter_teasericon_svg'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2048)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.teasericon')),
            ],
        ),
        migrations.DeleteModel(
            name='IndexText',
        ),
    ]
