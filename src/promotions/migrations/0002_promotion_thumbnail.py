# Generated by Django 2.0.4 on 2018-07-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='promo_images'),
        ),
    ]
