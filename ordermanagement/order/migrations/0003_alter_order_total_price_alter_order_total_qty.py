# Generated by Django 4.0.5 on 2022-07-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_total_price_alter_order_total_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_qty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
