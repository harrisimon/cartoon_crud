# Generated by Django 4.1 on 2022-11-19 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_character_voice_actor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='voice_actor',
        ),
    ]