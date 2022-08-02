from django.shortcuts import render
from .models import Tutor

# Create your views here.


def tutors(request):
    all_tutors = Tutor.objects.all()
    return render(request, 'tutors/tutors.html', {'all_tutors': all_tutors})

def tobetutors(request):
    return render(request, 'tutors/tobe_tutors.html')
