# Generated by Django 3.0.1 on 2020-10-29 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank='true', upload_to='images'),
        ),
    ]