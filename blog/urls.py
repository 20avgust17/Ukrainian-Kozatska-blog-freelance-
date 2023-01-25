from django.urls import path

from blog.views import IndexView, NewsDetailView, AboutView, ContactView, NewsListView, NewsByCategoryView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_pk'),
    path('category/<int:pk>/', NewsByCategoryView.as_view(), name='category'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
