# Generated by Django 3.2.18 on 2023-03-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
