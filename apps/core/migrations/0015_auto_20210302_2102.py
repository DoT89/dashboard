# Generated by Django 3.1.6 on 2021-03-02 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210302_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processstates',
            name='state_createdate',
        ),
        migrations.RemoveField(
            model_name='tshirtsizes',
            name='tshirt_createdate',
        ),
    ]
