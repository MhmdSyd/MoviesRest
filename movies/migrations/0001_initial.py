# Generated by Django 3.2.13 on 2022-04-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesRest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('poster', models.TextField()),
            ],
            options={
                'verbose_name': 'show',
                'ordering': ['-year', '-rating'],
            },
        ),
    ]