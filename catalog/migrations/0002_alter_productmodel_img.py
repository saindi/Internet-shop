# Generated by Django 4.1 on 2022-09-28 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='img',
            field=models.ImageField(default='category/img/logo.png', upload_to='catalog/img'),
        ),
    ]
