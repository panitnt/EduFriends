from django.shortcuts import get_object_or_404, render
from .models import Sheet

# Create your views here.
def sheet(request):
    all_sheet = Sheet.objects.all()
    return render(request, 'edu_sheet/sheet_home.html', {'all_sheet': all_sheet})

def sheet_details(request, sheet_id):
    detail = get_object_or_404(Sheet, pk=sheet_id)
    return render(request, 'edu_sheet/sheet_detail.html', {'detail': detail})

def share(request):
    return render(request, 'edu_sheet/sheet_share.html')