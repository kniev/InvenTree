# Generated by Django 4.2.16 on 2024-11-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0130_alter_parttesttemplate_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='partrelated',
            name='note',
            field=models.CharField(blank=True, help_text='Note for this relationship', max_length=500, verbose_name='Note'),
        ),
    ]