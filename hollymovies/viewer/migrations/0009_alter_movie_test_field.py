# Generated by Django 4.0.6 on 2022-07-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_movie_test_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='test_field',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
