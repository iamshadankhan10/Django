from django.shortcuts import render

# Create your views here.
def all_file(request):
    return render(request, 'file/all_file.html')