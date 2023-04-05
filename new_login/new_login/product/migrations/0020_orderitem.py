# Generated by Django 3.2.18 on 2023-04-04 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(max_length=12)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.order')),
            ],
        ),
    ]
