# Generated by Django 4.0.6 on 2022-07-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_alter_movie_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='average_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
