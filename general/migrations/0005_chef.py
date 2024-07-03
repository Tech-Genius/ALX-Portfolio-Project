# Generated by Django 4.1 on 2022-08-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_breakfast_dinner_lunch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('position', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='chef-images')),
                ('instagram', models.CharField(max_length=225)),
                ('twitter', models.CharField(max_length=225)),
                ('facebook', models.CharField(max_length=225)),
            ],
        ),
    ]
