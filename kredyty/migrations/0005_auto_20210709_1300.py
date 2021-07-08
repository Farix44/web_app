# Generated by Django 3.2.4 on 2021-07-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kredyty', '0004_alter_wnioski_kwota'),
    ]

    operations = [
        migrations.AddField(
            model_name='wnioski',
            name='imie',
            field=models.CharField(default=3, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wnioski',
            name='nazwisko',
            field=models.CharField(default=3, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wnioski',
            name='oprocentowanie',
            field=models.FloatField(default=8),
        ),
    ]
