from django.urls import path
from .views import *

app_name = 'onanasys'

urlpatterns = [
    path('newsAgents', NewsAgentsView.as_view()),
    path('newsArticles', NewsArticlesView.as_view()),
    path('articleComments', ArticleCommentsView.as_view()),
]