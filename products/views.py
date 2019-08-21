from django.shortcuts import render

def home(request):
    context ={
        #context
    }
    return render(request, 'products/home.html', context)
