# Generated by Django 3.1 on 2020-09-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_info', '0004_personalinfo_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='image',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]
