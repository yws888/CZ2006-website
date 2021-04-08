import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import HDBResaleFlat

class HDBResaleFlatTable(tables.Table):
    class Meta:
        model = HDBResaleFlat
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", )
        # fields = ("month", "" )
    Image = TemplateColumn(template_name='househunt/map_button.html')
    streetView = TemplateColumn(template_name='househunt/gmap_button.html')