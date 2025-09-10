from django.forms import ModelForm
from main.models import News

class NewsForm(ModelForm):
    class Meta:
        model = News    # menunjukkan model yang akan digunakan untuk form, daata yang disimpan dari form akan menjadi objek News
        fields = ["title", "content", "category", "thumbnail", "is_featured"]   # menunjukkan field dari model News yang digunakan untuk form. Field created_at dan news_views tidak dimasukkan ke list fields karena ditambahkan secara otomatis.
        