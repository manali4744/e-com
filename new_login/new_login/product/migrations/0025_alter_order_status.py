# Generated by Django 3.2.18 on 2023-04-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out of delivery', 'Out of delivery'), ('Delivered', 'Delivered')], default='Pending', max_length=250, null=True),
        ),
    ]
