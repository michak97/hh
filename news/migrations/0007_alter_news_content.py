# Generated by Django 5.2.4 on 2025-07-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_newstemplate_news_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.CharField(max_length=2048, verbose_name='Inhalt'),
        ),
    ]
