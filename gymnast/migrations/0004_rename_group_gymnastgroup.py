# Generated by Django 5.0.4 on 2024-06-06 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gymnast", "0003_group_alter_gymnast_grupp"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Group",
            new_name="GymnastGroup",
        ),
    ]
