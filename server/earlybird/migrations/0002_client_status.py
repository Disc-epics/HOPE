# Generated by Django 2.0 on 2019-03-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earlybird', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]