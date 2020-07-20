from django.views import generic
from music.models import import Album, Song








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
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html',
#                       {'album': album, 'error_message': "You did not selected a valid song"})
#     else:
#         selected.is_favorite = True
#         selected.save()
#         return render(request, 'music/detail.html', {'album': album})
