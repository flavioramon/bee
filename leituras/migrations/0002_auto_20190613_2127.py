# Generated by Django 2.2.2 on 2019-06-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leituras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leitura',
            name='nb_rssi',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='leitura',
            name='wb_rssi',
            field=models.CharField(max_length=50),
        ),
    ]