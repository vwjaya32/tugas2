from django.shortcuts import render
import mywatchlist
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all
    watchlist        = MyWatchList.objects.count()
    watched_count    = MyWatchList.objects.filter(watched=True).count()
    
    context = {
        'half_watched'  : True if watched_count >= (watchlist/2) else False,
        'h_nama'        : 'Nama:',
        'h_student_id'  : 'Student ID:',
        'list_film'     : data_mywatchlist,
        'nama'          : 'Vinsen Wijaya',
        'student_id'    : '2106637776'
    }
    return render (request, "mywatchlist.html", context)

def show_html(request):
    data = MyWatchList.objects.all
    context = {
        'list_film': data,
    }
    return render (request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")