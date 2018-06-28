# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-20 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        ('users', '0001_initial'),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartMessage',
            fields=[
                ('cart_id', models.AutoField(auto_created=True, db_column='cart_id', primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=100)),
                ('goods_num', models.IntegerField(default=0)),
                ('goods_xiaoji', models.FloatField()),
                ('goods_xprice', models.FloatField()),
                ('goods_pic', models.CharField(max_length=200)),
                ('goods', models.ForeignKey(db_column='goods_id', default='', on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfor')),
                ('manager', models.ForeignKey(db_column='manager_id', default='', on_delete=django.db.models.deletion.CASCADE, to='manager.ManagerLogin')),
                ('user', models.ForeignKey(db_column='user_id', default='', on_delete=django.db.models.deletion.CASCADE, to='users.UserB')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsAddress',
            fields=[
                ('address_id', models.AutoField(auto_created=True, db_column='address_id', primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=11)),
                ('user', models.ForeignKey(db_column='user_id', default='', on_delete=django.db.models.deletion.CASCADE, to='users.UserB')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(auto_created=True, db_column='order_id', primary_key=True, serialize=False)),
                ('order_num', models.CharField(max_length=50)),
                ('total', models.FloatField()),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_status', models.IntegerField(default=0)),
                ('address', models.ForeignKey(db_column='address_id', default='', on_delete=django.db.models.deletion.CASCADE, to='cart.GoodsAddress')),
                ('user', models.ForeignKey(db_column='user_id', default='', on_delete=django.db.models.deletion.CASCADE, to='users.UserB')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('details_id', models.AutoField(auto_created=True, db_column='details_id', primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=200)),
                ('goods_price', models.FloatField()),
                ('goods_num', models.IntegerField()),
                ('goods_xiaoji', models.FloatField()),
                ('goods_pic', models.CharField(max_length=200)),
                ('goods', models.ForeignKey(db_column='goods_id', default='', on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfor')),
                ('manager', models.ForeignKey(db_column='manager_id', default='', on_delete=django.db.models.deletion.CASCADE, to='manager.ManagerLogin')),
                ('order', models.ForeignKey(db_column='order_id', default='', on_delete=django.db.models.deletion.CASCADE, to='cart.Order')),
            ],
        ),
    ]