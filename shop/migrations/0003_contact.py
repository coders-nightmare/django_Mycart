# Generated by Django 3.0.5 on 2020-06-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200606_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]
