# Generated by Django 4.1.2 on 2022-10-10 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_app', '0005_character_background_character_job_character_race_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.SmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='character',
            name='constitution',
            field=models.SmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity',
            field=models.SmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='character',
            name='hitPoints',
            field=models.SmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.SmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.SmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom',
            field=models.SmallIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='character',
            name='job',
            field=models.CharField(default='class', max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(default='race', max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='skillProficiency',
            field=models.CharField(default='skill proficiency', max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='subrace',
            field=models.CharField(default='subrace', max_length=100),
        ),
    ]
