# Generated by Django 4.0.3 on 2022-04-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0006_destination_location_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('address', models.CharField(max_length=200, null=True)),
                ('offer', models.BooleanField(default=False)),
                ('location_type', models.CharField(max_length=100, null=True)),
                ('location_url', models.URLField(null=True)),
            ],
        ),
    ]
