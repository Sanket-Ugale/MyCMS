"""MyCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from MyCMS import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path("admin/", admin.site.urls),
    path('',views.homePage, name="home"),
    path('single-post/',views.LatestBlog, name="Post"),
    path('single-post/<newsSlug>',views.single_post, name="Post"),
    path('search-result/',views.search_result,name="Search"),
    path('comment/',views.comment,name="comment"),
    path('contact/',views.contact, name="contact"),
    path('category/',views.category,name="category"),
    path('about/',views.about,name="about"),
    # path('submitForm/',views.submitForm, name="submitForm"),
    path('calculator/',views.calculator, name="Calculator"),
    # path('headerCategory/',views.headerCategory, name="headerCategory")
]
# for image/file upload
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
