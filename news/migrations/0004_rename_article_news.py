# Generated by Django 5.1.5 on 2025-02-27 07:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_article_category_delete_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='News',
        ),
    ]
