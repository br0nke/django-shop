# Generated by Django 5.0.2 on 2024-02-26 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklisting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stock_listings/'),
        ),
    ]
