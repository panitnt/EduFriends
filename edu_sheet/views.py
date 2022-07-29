from django.shortcuts import render
from .models import Sheet

# Create your views here.
def sheet(request):
    all_sheet = Sheet.objects.all()
    return render(request, 'edu_sheet/sheet_home.html', {'all_sheet': all_sheet})