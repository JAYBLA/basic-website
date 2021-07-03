from django.shortcuts import render

def home(request):
    template_name = 'main/home.html'
    context = {
        'title':'Home',
    }
    return render(request, template_name, context)
