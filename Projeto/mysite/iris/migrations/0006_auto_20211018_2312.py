# Generated by Django 3.2.3 on 2021-10-19 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iris', '0005_auto_20211018_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='iris',
            name='iris_code',
            field=models.CharField(default='0101010', max_length=1000),
        ),
        migrations.AlterField(
            model_name='iris',
            name='chave_publica',
            field=models.CharField(default='chave', max_length=1000),
        ),
    ]