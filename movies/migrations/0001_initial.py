"""
This migration creates the initial schema for the Movies app.

Imports:
    migrations (django.db.migrations): The Django migrations module.
    models (django.db.models): The Django models module.

Migration Operations:
    CreateModel: Creates the Movie model with the specified fields.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    This class represents the initial migration for the Movies app.

    Attributes:
        initial (bool): Indicates that this is the initial migration.
        dependencies (list): A list of migration dependencies.
        operations (list): A list of operations to be applied in this migration.
    """

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("genre", models.CharField(max_length=100)),
                ("rating", models.FloatField()),
                ("release_date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
