# Generated by Django 3.1.2 on 2022-03-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.CharField(max_length=100),
        ),
    ]
