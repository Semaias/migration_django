# Generated by Django 2.2.4 on 2021-07-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZK', '0002_auto_20210702_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companieskfs',
            name='active',
            field=models.IntegerField(),
        ),
    ]