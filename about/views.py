from django.shortcuts import render
from django.contrib import messages
from . models import About, Proceedue, Testimonials, Team


def about(request):
    if request.method =='POST':
        name = request.POST['name']
        title = request.POST['title']
        description = request.POST['description']
        testimony = Testimonials(name=name, title=title, description=description)
        testimony.save()
        messages.success(request, ': We Appreciate Your Contribution')
    testimonials = Testimonials.objects.order_by('-added')
    about = About.objects.all()
    proceedue = Proceedue.objects.all()
    team = Team.objects.all()
    context = {
        'about':about,
        'proceedue':proceedue,
        'team':team,
        'testimonials':testimonials,
    }
       
    return render(request, 'pages/about.html', context)
