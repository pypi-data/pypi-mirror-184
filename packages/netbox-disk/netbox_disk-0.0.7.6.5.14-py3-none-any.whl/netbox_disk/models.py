from django.db import models, transaction
from django.urls import reverse

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search


class Disk(NetBoxModel):
    vg_name = models.CharField(
        unique=False,
        max_length=255,
    )
    lv_name = models.CharField(
        unique=False,
        max_length=255,
    )
    size = models.PositiveIntegerField(
        verbose_name="size",
        null=True,
        blank=True,
    )
    path = models.CharField(
        unique=False,
        max_length=255,
    )
    description = models.CharField(
        max_length=200,
        blank=True,
    )

    clone_fields = ["vg_name", "lv_name", "size", "path", "description"]

    def get_absolute_url(self):
        return reverse("plugins:netbox_disk:disk", kwargs={"pk": self.id})

    def __str__(self):
        return f"VM: test-vm vg_{self.vg_name}-lv_{self.lv_name}"

    class Meta:
        ordering = ("vg_name", "lv_name", "size", "path")


@register_search
class DiskIndex(SearchIndex):
    model = Disk
    fields = (
        ("vg_name", 100),
        ("lv_name", 150),
        ("size", 200),
    )
