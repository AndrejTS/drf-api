# Generated by Django 5.0.2 on 2024-02-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='attributes_ids',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='products_ids',
        ),
        migrations.AddField(
            model_name='catalog',
            name='attributes',
            field=models.ManyToManyField(to='app.attribute'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='products',
            field=models.ManyToManyField(to='app.product'),
        ),
    ]