# Generated by Django 4.0 on 2023-11-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
