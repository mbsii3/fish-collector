# Generated by Django 4.1.7 on 2023-03-16 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_decoration_alter_feeding_options_alter_feeding_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fish',
            old_name='decors',
            new_name='decorations',
        ),
    ]
