# Generated by Django 3.2 on 2021-07-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_qnt_in_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='info_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='info_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='info_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
