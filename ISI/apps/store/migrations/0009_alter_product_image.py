# Generated by Django 4.2.3 on 2024-03-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
