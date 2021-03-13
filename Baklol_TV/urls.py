"""Baklol_TV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from Baklol_TV import settings
from articlesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.trending,name="homepage"),
    path('about/',TemplateView.as_view(template_name="about_us.html"),name="about"),
    path('meet_our_developers/',TemplateView.as_view(template_name="developers.html"),name="meet_our_developers"),
    path('terms_and_conditions/',TemplateView.as_view(template_name="TermsAndConditions.html"),name="terms_and_conditions"),
    path('privacy_policy/',TemplateView.as_view(template_name="PrivacyPolicy.html"),name="privacy_policy"),
    path('', include('articlesapp.urls')),
    path('', include('videosapp.urls')),
    path('', include('memesapp.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)