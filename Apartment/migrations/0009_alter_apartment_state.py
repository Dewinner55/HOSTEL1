# Generated by Django 4.1.7 on 2023-03-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Apartment", "0008_alter_apartment_zip_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apartment",
            name="state",
            field=models.CharField(
                help_text="Необязательно поле для заполнения",
                max_length=100,
                verbose_name="Округ",
            ),
        ),
    ]
