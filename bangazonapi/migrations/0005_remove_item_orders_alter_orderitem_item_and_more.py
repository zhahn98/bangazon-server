# Generated by Django 4.1.3 on 2024-01-15 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0004_rename_item_id_orderitem_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='orders',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.item'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.order'),
        ),
    ]
