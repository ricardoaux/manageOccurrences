# Generated by Django 2.1 on 2018-08-09 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20180809_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
