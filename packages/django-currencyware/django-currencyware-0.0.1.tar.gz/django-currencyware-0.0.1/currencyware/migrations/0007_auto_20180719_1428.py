# Generated by Django 2.0.6 on 2018-07-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencyware', '0006_auto_20180710_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='name',
            field=models.CharField(blank=True, help_text='Curreny name (english)', max_length=100, null=True, verbose_name='Name'),
        ),
    ]
