# Generated by Django 4.1 on 2022-09-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_percentage_discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='percentage_days_left',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='percentage_off',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_after_percentage_discount',
            field=models.CharField(max_length=205, null=True),
        ),
    ]
