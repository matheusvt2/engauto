# Generated by Django 3.2.8 on 2021-10-18 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211014_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='published',
        ),
        migrations.AddField(
            model_name='history',
            name='terminal_error',
            field=models.CharField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='history',
            name='terminal',
            field=models.CharField(max_length=5000),
        ),
    ]