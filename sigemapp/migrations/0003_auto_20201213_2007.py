# Generated by Django 3.1.4 on 2020-12-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigemapp', '0002_auto_20201213_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='fecha_revision',
            field=models.DateTimeField(verbose_name='fecha de revision'),
        ),
    ]
