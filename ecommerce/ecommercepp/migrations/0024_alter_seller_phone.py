# Generated by Django 4.0.6 on 2022-08-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommercepp", "0023_alter_seller_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seller",
            name="phone",
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
