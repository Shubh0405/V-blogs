# Generated by Django 3.1 on 2020-08-17 21:18

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20200818_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]