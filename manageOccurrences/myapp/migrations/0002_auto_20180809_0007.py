# Generated by Django 2.1 on 2018-08-08 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occurrence',
            old_name='author_id',
            new_name='author',
        ),
    ]