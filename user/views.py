from django.http import HttpResponse
from django.shortcuts import render,redirect


def index(request):
    if request.method == 'POST':
        print(request.POST['careeerObjective'])
    return render (request=request, template_name="profile.html")
