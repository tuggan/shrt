# Generated by Django 3.0.7 on 2020-07-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='times_visited',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(),
        ),
    ]