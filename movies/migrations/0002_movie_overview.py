"""
This migration adds the 'overview' field to the Movie model.

Imports:
    migrations (django.db.migrations): The Django migrations module.
    models (django.db.models): The Django models module.

Migration Dependencies:
    0001_initial: The initial migration for the Movies app.

Migration Operations:
    AddField: Adds the 'overview' field to the Movie model.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    This class represents the migration to add the 'overview' field to the Movie model.

    Dependencies:
        0001_initial: The initial migration for the Movies app.

    Operations:
        AddField: Adds the 'overview' field to the Movie model.
    """

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="overview",
            field=models.TextField(default=""),
        ),
    ]
