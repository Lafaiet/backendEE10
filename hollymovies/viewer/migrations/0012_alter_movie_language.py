# Generated by Django 4.0.6 on 2022-07-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0011_movie_trailer_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(blank=True, default='english', max_length=30, null=True),
        ),
    ]
