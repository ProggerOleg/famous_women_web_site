# Generated by Django 4.0.4 on 2022-06-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_women_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
