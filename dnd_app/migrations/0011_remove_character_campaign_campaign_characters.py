# Generated by Django 4.1.2 on 2022-10-12 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_app', '0010_alter_campaign_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='campaign',
        ),
        migrations.AddField(
            model_name='campaign',
            name='characters',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dnd_app.character'),
        ),
    ]
