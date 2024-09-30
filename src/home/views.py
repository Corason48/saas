from django.shortcuts import render
from django.http import HttpResponse
from visits.models import Visit
def home_view(request,*args, **kwargs):
    return about_view(request,*args, **kwargs)
def about_view(request,*args, **kwargs):
    
    html='test.html'
    # Visit.objects.create()
    query = Visit.objects.all()
    title={"title":query}
    return render(request,html,title)