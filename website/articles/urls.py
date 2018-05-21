
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

    path('', views.ArticleListView.as_view(), name='home' ),
    path('projekt/', views.ProjektView.as_view(), name='projekt' ),
    path('image/', views.ImageView.as_view(), name='images' ),
    path('settings/', views.SettingsView.as_view(), name='settings' ),
    path('new/', views.NewView.as_view(), name='new' ),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_page' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
