# Generated by Django 3.1.1 on 2020-11-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
