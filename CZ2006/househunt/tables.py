import django_tables2 as tables
from .models import HDBResaleFlat

class HDBResaleFlatTable(tables.Table):
    class Meta:
        model = HDBResaleFlat
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", )
        # fields = ("month", "" )