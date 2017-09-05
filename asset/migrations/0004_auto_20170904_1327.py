# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20170903_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='system_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='用户别称')),
                ('username', models.CharField(max_length=64, verbose_name='登陆用户')),
                ('password', models.CharField(blank=True, max_length=256, verbose_name='登陆密码')),
            ],
            options={
                'verbose_name': '系统登陆用户',
                'verbose_name_plural': '系统登陆用户',
                'db_table': 'system_users',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='system',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='系统'),
        ),
        migrations.AddField(
            model_name='asset',
            name='uplink_port',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='上联端口'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='port',
            field=models.IntegerField(blank=True, null=True, verbose_name='ssh端口'),
        ),
        migrations.AddField(
            model_name='asset',
            name='system_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.system_users', verbose_name='登陆用户'),
        ),
    ]