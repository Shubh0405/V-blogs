# Generated by Django 3.1 on 2020-08-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20200818_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(allow_unicode=True, editable=False, unique=True),
        ),
    ]
