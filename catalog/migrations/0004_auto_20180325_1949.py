# Generated by Django 2.0.3 on 2018-03-25 19:49

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180310_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelperson',
            name='bio',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='modelperson',
            name='profile_pic',
            field=s3direct.fields.S3DirectField(default=''),
            preserve_default=False,
        ),
    ]