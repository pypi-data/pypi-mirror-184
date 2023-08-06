from netbox.views import generic

from netbox_disk.filters import DiskFilter
from netbox_disk.forms import (
    DiskImportForm,
    DiskFilterForm,
    DiskForm,
    DiskBulkEditForm
)
from netbox_disk.models import Disk
from netbox_disk.tables import DiskTable


class DiskListView(generic.ObjectListView):
    queryset = Disk.objects
    filterset = DiskFilter
    filterset_form = DiskFilterForm
    table = DiskTable


class DiskView(generic.ObjectView):
    """Display Disk details"""

    queryset = Disk.objects.all()


class DiskEditView(generic.ObjectEditView):
    """View for editing a Disk instance."""

    queryset = Disk.objects
    form = DiskForm
    default_return_url = "plugins:netbox_disk:disk_list"


class DiskDeleteView(generic.ObjectDeleteView):
    queryset = Disk.objects
    default_return_url = "plugins:netbox_disk:disk_list"


class DiskBulkImportView(generic.BulkImportView):
    queryset = Disk.objects
    model_form = DiskImportForm
    table = DiskTable
    default_return_url = "plugins:netbox_disk:disk_list"


class DiskBulkEditView(generic.BulkEditView):
    queryset = Disk.objects
    filterset = DiskFilter
    table = DiskTable
    form = DiskBulkEditForm


class DiskBulkDeleteView(generic.BulkDeleteView):
    queryset = Disk.objects
    table = DiskTable
