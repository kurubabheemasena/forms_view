# Generated by Django 4.1.5 on 2023-02-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]