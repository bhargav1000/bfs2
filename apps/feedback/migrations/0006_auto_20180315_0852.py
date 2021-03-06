# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-15 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_auto_20180306_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackform',
            name='recipient',
            field=models.ForeignKey(help_text='Type of user that is receiving the feedback for this form', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form', to='general.UserType'),
        ),
    ]
