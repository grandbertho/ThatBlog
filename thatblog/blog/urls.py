from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('all_articles/', views.all_articles, name='all_articles'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),  # Page de détail d'article
    path('create/', views.create_article, name='create_article'),  # Page pour ajouter des articles
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('category/<int:category_id>/', views.articles_by_category, name='articles_by_category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)