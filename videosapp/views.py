from django.core.paginator import Paginator
from django.shortcuts import render
from videosapp.models import *

# Create your views here.
def videos(request):
    videos_data = VideosModel.objects.filter(is_published=True)

    paginator = Paginator(videos_data, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"videos_templates/videos_homepage.html",context)