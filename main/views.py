from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406418774',
        'name': 'Cathlin Abigail',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)

# request: Ini adalah objek permintaan HTTP yang dikirim oleh pengguna
# main.html: Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.
# context: Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.
