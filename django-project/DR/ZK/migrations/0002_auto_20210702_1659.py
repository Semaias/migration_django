# Generated by Django 2.2.4 on 2021-07-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZK', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companieskfs',
            name='active',
            field=models.IntegerField(max_length=1),
        ),
    ]