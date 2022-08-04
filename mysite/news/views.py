from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news.html'
    context_object_name = 'news'

    # extra_context = {'title': 'Главная'} #Для статичных данных

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ClCategory(ListView):
    model = News
    template_name = 'news/home_news.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    #success_url = reverse_lazy('home')


'''def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request=request, template_name='news/index.html', context=context)'''

'''def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, template_name='news/category.html', context={'news': news,
                                                                        'category': category})'''

'''def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, template_name='news/view_news.html', context={'news_item': news_item})'''

'''def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # WithOutModel
            # news = News.objects.create(**form.cleaned_data)
            # WithModel
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, template_name='news/add_news.html', context={'form': form})
'''
