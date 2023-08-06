import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name="Disk",
            fields=[
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("vg_name", models.CharField(max_length=255)),
                ("lv_name", models.CharField(max_length=1000)),
                ("size", models.PositiveIntegerField()),

            ],
            options={
                "ordering": ("lv_name", "id"),
            },
        ),
    ]