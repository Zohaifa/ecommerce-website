# Generated by Django 5.1.4 on 2024-12-17 13:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('QR', 'Quran'), ('SH', 'Sihah Sittah'), ('HH', 'Hadith Books'), ('DU', 'Dua Compilation')], max_length=2),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Chittagong', 'Chittagong'), ('Dhaka', 'Dhaka'), ('Sylhet', 'Sylhet'), ('Barisal', 'Barisal'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur')], max_length=108)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
