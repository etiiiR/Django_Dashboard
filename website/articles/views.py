from django.views.generic import ListView, DetailView

# Create your views here.

from . models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'batman'

class ProjektView(ListView):
    model = Article
    template_name = 'projekt.html'


class ImageView(ListView):
    model = Article
    template_name = 'image.html'

class SettingsView(ListView):
    model = Article
    template_name = 'settings.html'

class NewView(ListView):
    model = Article
    template_name = 'new.html'