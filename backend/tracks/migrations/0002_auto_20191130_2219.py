# Generated by Django 2.2.7 on 2019-11-30 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackstates',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]