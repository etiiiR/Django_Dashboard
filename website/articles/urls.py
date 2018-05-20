
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

    path('', views.ArticleListView.as_view(), name='home' ),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_page' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
