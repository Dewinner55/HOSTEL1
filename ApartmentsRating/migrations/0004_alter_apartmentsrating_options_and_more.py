# Generated by Django 4.1.7 on 2023-03-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ApartmentsRating", "0003_alter_apartmentsrating_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="apartmentsrating",
            options={},
        ),
        migrations.AlterField(
            model_name="apartmentsrating",
            name="rating",
            field=models.FloatField(
                help_text="Введите рейтинг от 1.0 до 5.0, например, 3.5"
            ),
        ),
    ]
