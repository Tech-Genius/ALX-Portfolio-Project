# Generated by Django 4.1 on 2022-09-04 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_remove_product_category_delete_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Popular',
        ),
    ]
