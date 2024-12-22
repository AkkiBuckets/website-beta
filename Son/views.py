from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def linux_cheat_sheet(request):
    return render(request, 'linux_cheat_sheet.html')

def useful_links(request):
    return render(request, 'useful_links.html')