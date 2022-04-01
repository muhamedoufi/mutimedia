from django.shortcuts import render

# Create your views here.
def showImages(request):
    return render(request, 'image/images.html',{"title":"Images"})
