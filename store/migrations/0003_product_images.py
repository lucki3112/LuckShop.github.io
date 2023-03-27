# Generated by Django 4.1.7 on 2023-03-15 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_images', models.FileField(upload_to='product_image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]