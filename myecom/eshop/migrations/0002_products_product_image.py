# Generated by Django 4.0.4 on 2022-04-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]