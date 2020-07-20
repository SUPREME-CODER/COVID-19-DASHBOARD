from django.shortcuts import render, HttpResponse

# Create your views here.
def analysis(request):
    return render(request, 'firstUI/analysis.html')

def about(request):
    return render(request, 'firstUI/developer.html')