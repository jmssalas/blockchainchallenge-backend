# Generated by Django 2.2.7 on 2019-11-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191130_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]