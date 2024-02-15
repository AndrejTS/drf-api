# Generated by Django 5.0.2 on 2024-02-12 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeName',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=255, null=True)),
                ('zobrazit', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hodnota', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=255, null=True)),
                ('obrazek', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mena', models.CharField(max_length=3, null=True)),
                ('is_published', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev_atributu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attributename')),
                ('hodnota_atributu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.attributevalue')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=255, null=True)),
                ('products_ids', models.JSONField(null=True)),
                ('attributes_ids', models.JSONField(null=True)),
                ('obrazek_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.image')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(related_name='products', through='app.ProductAttributes', to='app.attribute'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=255)),
                ('obrazek_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
