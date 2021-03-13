from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from articlesapp.models import *
from videosapp.models import *
import itertools
from django.db.models import Q

# Create your views here.
def trending(request):
    data = ArticlesModel.objects.filter(is_trending=True,is_published=True)
    carousel_data = CarouselModel.objects.filter(is_published=True)
    videos = VideosModel.objects.filter(is_published=True,is_trending=True)
    trending_videos = itertools.islice(videos, 15)
    res = list(itertools.islice(reversed(carousel_data), 0, 3))
    l = []
    for x in  res:
        l.append(x)

    slide1 = l[0]
    slide2 = l[1]
    slide3 = l[2]
    paginator = Paginator(data, 40)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"page_obj":page_obj,"trending_videos":trending_videos,"slide1":slide1,"slide2":slide2,"slide3":slide3}
    return render(request,"homepage.html",context)


def stories(request):
    articles_data = ArticlesModel.objects.filter(is_published=True)
    carousel_data = CarouselModel.objects.filter(is_published=True)
    res = list(itertools.islice(reversed(carousel_data), 0, 3))
    l = []
    for x in res:
        l.append(x)
    slide1 = l[0]
    slide2 = l[1]
    slide3 = l[2]

    paginator = Paginator(articles_data, 60)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"page_obj":page_obj,"slide1":slide1,"slide2":slide2,"slide3":slide3}
    return render(request,"articles_templates/article_homepage.html",context)


def single_article(request,id):
    article = ArticlesModel.objects.get(id=id)
    trending_data = ArticlesModel.objects.filter(is_trending=True, is_published=True)
    top10 = itertools.islice(trending_data, 10)
    context = {"article": article,"trending_data":top10}

    return render(request,"articles_templates/single_article.html",context)


def single_carousel_article(request,id):
    article = CarouselModel.objects.get(id=id)
    trending_data = ArticlesModel.objects.filter(is_trending=True, is_published=True)
    top10 = itertools.islice(trending_data, 10)
    context = {"article": article, "trending_data": top10}

    return render(request, "articles_templates/single_article.html", context)


def search_article(request):
    s = request.POST.get("search")
    if s:
        src = ArticlesModel.objects.filter(Q(tittle__icontains=s) | Q(category__icontains=s))
        if src:
            return render(request, "articles_templates/search.html", {"src": src,"search":s})
        else:
            return render(request,"articles_templates/search.html",{"message":" Sorry we couldn't find any matches for, "+s,"search":s})
    else:
        return redirect("homepage")

