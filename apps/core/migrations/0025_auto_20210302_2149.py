# Generated by Django 3.1.6 on 2021-03-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20210302_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstates',
            name='state_createdate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation Date'),
        ),
    ]
