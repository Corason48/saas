from django.shortcuts import render
from django.http import HttpResponse
from visits.models import Visit
def get_home_view(request,*args, **kwargs):
    
    html='test.html'
    # Visit.objects.create()
    query = Visit.objects.all()
    title={"title":query}
    return render(request,html,title)