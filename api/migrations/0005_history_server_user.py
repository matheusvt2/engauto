# Generated by Django 3.2.8 on 2021-10-18 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211018_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='server_user',
            field=models.CharField(default='user', max_length=60),
            preserve_default=False,
        ),
    ]