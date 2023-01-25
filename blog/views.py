from django.views.generic import DetailView, TemplateView, ListView, CreateView
from blog.forms import FeedBackForm
from blog.models import Blog


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = Blog.objects.all().order_by('-pk')[:4]
        context['title'] = 'Винницкое Козачество'
        return context


class NewsListView(ListView):
    template_name = "news.html"
    queryset = 'news_list'

    def get_queryset(self):
        return Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = Blog.objects.all().order_by('-pk')
        context['title'] = 'Список новостей'
        return context


class NewsByCategoryView(ListView):
    template_name = "news_by_category.html"
    queryset = 'news_list'
    context_object_name = 'news_by_category'

    def get_queryset(self):
        return Blog.objects.filter(category_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория'
        return context


class NewsDetailView(DetailView):
    model = Blog
    template_name = "news_detail.html"
    context_object_name = 'item'

    def get_queryset(self):
        return Blog.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        return context


class ContactView(CreateView):
    form_class = FeedBackForm
    template_name = 'contact.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакти'
        return context
