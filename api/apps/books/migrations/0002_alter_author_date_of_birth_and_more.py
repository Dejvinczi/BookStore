# Generated by Django 5.0.6 on 2024-06-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="date_of_birth",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="book",
            name="publication_date",
            field=models.DateField(),
        ),
    ]
