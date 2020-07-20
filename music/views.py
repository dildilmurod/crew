from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from music.models import Album, Song


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'genre', 'album_title', 'album_logo']





# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from music.models import Album, Song
# from django.http import Http404
# from django.template import loader
#
#
# def index(request):
#     all_albums = Album.objects.all()
#     context = {
#         'all_albums': all_albums,
#     }
#     return render(request, 'music/index.html', context)
#
#
# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album': album})
#
