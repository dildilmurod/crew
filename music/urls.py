from . import views
from django.urls import path

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # register
    path('register/', views.UserFormView.as_view(), name='register'),

    # /music/id
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /music/album/add
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/id
    path('album/<int:pk>', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/id/delete
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),


    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
