from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'cards/index.html')

def reports(request):
    return render(request, 'cards/reports.html')