# Generated by Django 4.1.2 on 2022-10-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_actor_image_alter_movie_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='fees_in_world',
            field=models.PositiveIntegerField(default=0, help_text='Укажите сумму в доларах', verbose_name='Сборы в Мире'),
        ),
    ]