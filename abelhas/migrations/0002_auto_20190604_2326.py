# Generated by Django 2.2.1 on 2019-06-04 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abelhas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abelha',
            options={'ordering': ['-id']},
        ),
    ]
