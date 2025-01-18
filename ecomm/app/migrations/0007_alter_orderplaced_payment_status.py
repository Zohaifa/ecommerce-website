# Generated by Django 5.1.4 on 2025-01-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_orderplaced_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='payment_status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
