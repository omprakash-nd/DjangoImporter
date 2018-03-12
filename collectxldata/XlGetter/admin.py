from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ControlPlan

# Register your models here.
@admin.register(ControlPlan)
class ControlPlanAdmin(ImportExportModelAdmin):
    pass
    # class Meta:
    #     model = TrainInfo
    #     fields = ('Trainno', 'Depature', 'DepatureTime', 'Arrival', 'ArrivalTime', )
    #     export_order = ('Depature', 'DepatureTime', 'Arrival', 'ArrivalTime', 'Trainno',)
    #     admin.site.register(model)