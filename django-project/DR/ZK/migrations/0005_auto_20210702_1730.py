# Generated by Django 2.2.4 on 2021-07-02 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZK', '0004_auto_20210702_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companieskfs',
            name='active',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='companieskfs',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='companieskfs',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='companieskfs',
            name='version',
            field=models.SmallIntegerField(default=3),
        ),
    ]