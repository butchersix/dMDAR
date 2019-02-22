# Generated by Django 2.0.7 on 2019-02-17 16:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobi', '0006_auto_20190218_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='display_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]