from django.shortcuts import render
from .models import Room

# Create your views here.
def study_room(request):
    room = Room.objects.all()
    return render(request, 'study_room/study_room.html', {'rooms': room})

def create_room(request):
    return render(request, 'study_room/create_room.html')