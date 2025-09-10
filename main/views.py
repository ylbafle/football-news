from django.shortcuts import render, redirect, get_object_or_404
from main.forms import NewsForm
from main.models import News
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    news_list = News.objects.all()  # untuk mengambil seluruh objek News yang tersimpan pada database

    context = {
        'npm' : '2406418774',
        'name': 'Cathlin Abigail',
        'class': 'PBP A',
        'news_list': news_list
    }

    return render(request, "main.html", context)

# request: Ini adalah objek permintaan HTTP yang dikirim oleh pengguna
# main.html: Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.
# context: Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.

def create_news(request):
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_news.html", context)

def show_news(request, id):
    news = get_object_or_404(News, pk=id)   # mengambil objek News berdasarkan primary key (id). Jika objek tidak ditemukan, akan mengembalikan halaman 404.
    news.increment_views()                  # menambah jumlah views

    context = {
        'news': news
    }

    return render(request, "news_detail.html", context)

def show_xml(request):
    news_list = News.objects.all()
    xml_data = serializers.serialize("xml", news_list)  #  translate objek model menjadi format lain seperti dalam fungsi ini adalah XML.   
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    news_list = News.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, news_id):
   try:
       news_item = News.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", news_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except News.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, news_id):
   try:
       news_item = News.objects.get(pk=news_id)
       json_data = serializers.serialize("json", [news_item])
       return HttpResponse(json_data, content_type="application/json")
   except News.DoesNotExist:
       return HttpResponse(status=404)