# Generated by Django 3.2.13 on 2022-05-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('year_joined', models.CharField(max_length=4)),
            ],
        ),
    ]
