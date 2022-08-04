from django.urls import path

from .views import *

urlpatterns = [
    #path('', index, name='home'), #WithOutListView
    #path('category/<int:category_id>/', get_category, name='category'), #WithOutListView
    #path('news/<int:news_id>/', view_news, name='view_news'), #WithOutListView
    #path('news/add_news/', add_news, name='add_news'), #WithOutListView
    path('', HomeNews.as_view(), name='home'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('category/<int:category_id>/', ClCategory.as_view(), name='category'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
]