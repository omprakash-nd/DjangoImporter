from import_export import resources
from .models import ControlPlan

class ControlPlanResource(resources.ModelResource):
    class Meta:
        model = ControlPlan
        
