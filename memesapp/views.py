from django.shortcuts import render
from memesapp.models import *

# Create your views here.
def memes_home(request):
    memes = MemesModel.objects.all()
    context ={"memes":memes}
    return render(request,"memes_templates/memes_homepage.html",context)


def single_meme(request,id):
    meme = MemesModel.objects.get(id=id)

    return render(request,"memes_templates/single_meme.html",{"meme":meme})