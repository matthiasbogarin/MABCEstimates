# Generated by Django 3.2.8 on 2022-06-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimates',
            fields=[
                ('estimateId', models.AutoField(primary_key=True, serialize=False)),
                ('estimateName', models.CharField(max_length=100)),
            ],
        ),
    ]
