# Generated by Django 4.1 on 2022-11-19 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_remove_character_voice_actor'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoiceActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='voice_actor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='characters.voiceactor'),
            preserve_default=False,
        ),
    ]
