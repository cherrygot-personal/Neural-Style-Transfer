# Generated by Django 2.2.5 on 2019-10-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media_model',
            name='preview',
            field=models.ImageField(null=True, upload_to='preview/'),
        ),
    ]
