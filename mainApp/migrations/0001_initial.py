# Generated by Django 2.0.5 on 2018-12-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('dsg', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
