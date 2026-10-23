from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.get_song_list, name='song-list'),
    path('songs/create/', views.create_song, name='song-create'),
    path('songs/<int:pk>/', views.get_one_song, name='song-by-id'),
    path('songs/<int:pk>/delete/', views.delete_song, name='song-delete'),
    path('songs/<int:pk>/update/', views.update_song, name='song-update'),
    path('songs/search/', views.search_song, name='song-search'),
    path('spotify/track/<str:track_id>/', views.get_spotify_track, name='spotify-track'),
    path('spotify/import/', views.import_song, name='spotify-import'),

]