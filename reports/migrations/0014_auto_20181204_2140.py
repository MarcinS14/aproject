# Generated by Django 2.1 on 2018-12-04 21:40

from django.db import migrations, models
import reports.models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0013_auto_20181204_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportsent',
            name='file',
            field=models.FileField(max_length=200, upload_to=reports.models.user_directory_path),
        ),
    ]
