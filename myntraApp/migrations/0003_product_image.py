# Generated by Django 5.0 on 2024-01-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myntraApp', '0002_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
