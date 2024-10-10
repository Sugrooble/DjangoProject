# Generated by Django 5.1.1 on 2024-10-09 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0007_husband_women_husband'),
    ]

    operations = [
        migrations.AddField(
            model_name='husband',
            name='marriage_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='women',
            name='husband',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='woman', to='women.husband'),
        ),
    ]