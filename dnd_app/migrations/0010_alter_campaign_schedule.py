# Generated by Django 4.1.2 on 2022-10-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_app', '0009_character_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='schedule',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=100),
        ),
    ]
