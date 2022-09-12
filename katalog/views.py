from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'list_item': data_item_katalog,
        'nama': 'Vinsen Wijaya',
        'student_id': '2106637776'
    }
    return render(request, "katalog.html", context)