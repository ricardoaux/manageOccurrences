# Generated by Django 2.1 on 2018-08-09 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180809_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occurrence',
            old_name='author',
            new_name='author_id',
        ),
    ]