from django.shortcuts import render
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from .spotify import get_track, extract_spotify_id

# Create your views here.
@api_view(['GET'])
def get_song_list(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_song(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_one_song(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response(status=404)
    
    serializer = SongSerializer(song)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_song(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response(status=404)
    
    song.delete()
    return Response(status=204)

@api_view(['PUT'])
def update_song(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response(status=404)
    serializer = SongSerializer(song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def search_song(request):
    query = request.GET.get('q', '')
    songs = Song.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query) | Q(album__icontains=query))
    serializer = SongSerializer(songs, many=True)
    # print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def get_spotify_track(request, track_id):
    track_data = get_track(track_id)
    return Response(track_data)

@api_view(['POST'])
def import_song(request):

    spotify_url = request.data.get('spotify_url')
    track_id = extract_spotify_id(spotify_url)
    track_data = get_track(track_id)

    if Song.objects.filter(spotify_id=track_id).exists():
        return Response({"error": "Song already exists in the database."}, status=400)
    
    if "error" in track_data:
        return Response({"error": track_data["error"]}, status=400)
    
    song = Song.objects.create(
        title=track_data["title"],
        artist=track_data["artist"],
        album=track_data["album"],
        release_date=track_data["release_date"],
        genre="Unknown",
        spotify_id=track_id
    )

    serializer = SongSerializer(song)
    return Response(serializer.data, status=201)