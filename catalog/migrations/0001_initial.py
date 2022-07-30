# Generated by Django 4.0.6 on 2022-07-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
