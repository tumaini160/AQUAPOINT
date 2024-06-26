# Generated by Django 5.0.4 on 2024-06-09 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10000)),
                ('Number', models.PositiveIntegerField()),
                ('Coordinates', models.CharField(max_length=1000000)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Coordinates', models.CharField(max_length=1000000)),
                ('SensorValue', models.PositiveIntegerField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
