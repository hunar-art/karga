# Generated by Django 3.2 on 2021-07-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpermission',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
