# Generated by Django 3.0.7 on 2020-07-06 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0003_auto_20200704_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('source', models.GenericIPAddressField()),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=2)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='url.Url')),
            ],
        ),
    ]
