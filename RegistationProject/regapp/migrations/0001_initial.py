# Generated by Django 5.0.2 on 2024-03-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EName', models.CharField(max_length=30)),
                ('Enumber', models.IntegerField()),
                ('EAddress', models.CharField(max_length=30)),
                ('Esal', models.FloatField()),
            ],
        ),
    ]