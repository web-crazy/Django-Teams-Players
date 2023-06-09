# Generated by Django 3.2.9 on 2023-05-10 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('mascot', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeamContainsPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teams.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teams.team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(blank=True, related_name='player', through='Teams.TeamContainsPlayer', to='Teams.Player'),
        ),
    ]
