import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import HDBResaleFlat

class HDBResaleFlatTable(tables.Table):
    class Meta:
        model = HDBResaleFlat
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", )
        # fields = ("month", "" )
    image = TemplateColumn(template_name='househunt/map_button.html')
