# Generated by Django 2.0.4 on 2018-08-12 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0007_auto_20180731_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='promo_images/full/'),
        ),
    ]
