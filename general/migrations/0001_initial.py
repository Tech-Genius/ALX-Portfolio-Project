# Generated by Django 4.1 on 2022-08-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('days_left', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='promo_images')),
                ('percentage_off', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=205)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
