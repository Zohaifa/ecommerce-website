# Generated by Django 5.1.4 on 2024-12-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('QR', 'Quran'), ('BH', 'Bukhari'), ('MS', 'Muslim'), ('HM', 'Hisnul Muslim'), ('BM', 'Bulugul Maram'), ('JT', 'Jamii Tirmidhi'), ('MA', 'Musnad Ahmed')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
