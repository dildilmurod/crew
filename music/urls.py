from . import views
from django.urls import path

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/id
    path('<int:album_id>/', views.detail, name='detail'),

    # /music/id/favorite/
    path('<int:album_id>/favorite/', views.favorite, name='favorite'),

    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
