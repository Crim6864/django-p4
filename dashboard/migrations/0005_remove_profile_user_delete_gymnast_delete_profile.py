# Generated by Django 5.0.4 on 2024-05-11 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0004_alter_gymnast_efternamn_alter_gymnast_förnamn_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Gymnast",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
