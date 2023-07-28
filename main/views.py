from django.shortcuts import render
def home(request):
    return render(request, 'main/home.html')
def kontakty(request):
    return render(request, 'main/kontakty.html')