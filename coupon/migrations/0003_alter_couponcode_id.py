# Generated by Django 3.2.4 on 2022-01-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_alter_couponcode_discounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponcode',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
