from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from MyCMS.forms import userForm
from blog.models import blog
from django.core.paginator import Paginator

from comments.models import commentsModel
from django.core.mail import send_mail

def homePage(request):
    Categories=blog.objects.values('category').distinct().order_by('category')[:1]
    # - is used to pass deta in decending order
    # [:5 is to Select only first 5 data]
    categoryData = blog.objects.all().order_by('category').values().distinct()
    latestBlogData=blog.objects.all().order_by('-id')[:5]
    # print(categoryData)
    data={
        "title":"ZenBlog | Home",
        'latestBlogData':latestBlogData,
        'Categories':Categories,
        'categoryData':categoryData
    }
    return render(request,"index.html",data)

def LatestBlog(request):
    blogData=blog.objects.all().order_by('-id')[0]
    Categories=blog.objects.values('category').distinct()
    latestBlogData=blog.objects.all().order_by('-id')[:5]
    commentsData=commentsModel.objects.filter(url=blogData.url)
    data={
        "title":"ZenBlog | Blog",
        'blogData':blogData,
        "commentsData":commentsData,
        'Categories':Categories,
        'latestBlogData':latestBlogData
    }
    return render(request,"latestBlog.html",data)

def single_post(request,newsSlug):
    singleBlogData=blog.objects.get(url=newsSlug)
    commentsData=commentsModel.objects.filter(url=newsSlug)
    Categories=blog.objects.values('category').distinct()
    latestBlogData=blog.objects.all().order_by('-id')[:5]
        # print(newsSlug,"SLUUUUUUUUUUR")
    # print("COMMENT: ",commentsData.message)
    data={
            "title":"ZenBlog | Blog",
            "singleBlogData":singleBlogData,
            "commentsData":commentsData,
            "Categories":Categories,
            "latestBlogData":latestBlogData,
    }       
    return render(request,"single-post.html",data)

def search_result(request):
    # print('search_result')
    if request.method=="GET":
        data={}
        searchData=request.GET.get('searchData')
        if searchData!=None:
            searchedRlt=blog.objects.filter(Title__icontains=searchData)
            Categories=blog.objects.values('category').distinct()
            latestBlogData=blog.objects.all().order_by('-id')[:5]
            paginator=Paginator(searchedRlt,3)
            page_number=request.GET.get('page')
            searchedResult=paginator.get_page(page_number)
            totalPages=searchedResult.paginator.num_pages
            data={
            "title":"ZenBlog | Search Result",
            # "searchedResult":searchedResult,
            "searchedResult":searchedResult,
             # bysearch is used for pagination
            "bySearch":True,
            "searchData":searchData,
            "lastPage":totalPages,
            "totalPageList":[n+1 for n in range(totalPages)],
            "Categories":Categories,
            "latestBlogData":latestBlogData,
            }
            return render(request,"search-result.html",data)
        else:
            Categories=blog.objects.values('category').distinct()
            latestBlogData=blog.objects.all().order_by('-id')[:5]
            searchedRlt=blog.objects.all()
            paginator=Paginator(searchedRlt,3)
            page_number=request.GET.get('page')
            searchedResult=paginator.get_page(page_number)
            totalPages=searchedResult.paginator.num_pages
            data={
                "title":"ZenBlog | Search Result",
                "searchedResult":searchedResult,
                # bysearch is used for pagination
                "bySearch":False,
                "lastPage":totalPages,
                "totalPageList":[n+1 for n in range(totalPages)],
                "Categories":Categories,
                "latestBlogData":latestBlogData,
            }
            return render(request,"search-result.html",data)

def category(request):
    Categories=blog.objects.values('category').distinct()
    latestBlogData=blog.objects.all().order_by('-id')[:5]
    category=request.GET.get('category')
    categoryData=blog.objects.filter(category__icontains=category)
    data={
        "title":"ZenBlog | Category",
        "categoryData":categoryData,
        "category":category,
        "Categories":Categories,
        "latestBlogData":latestBlogData,
    }
    return render(request,"category.html",data)

def about(request):
    Categories=blog.objects.values('category').distinct()
    latestBlogData=blog.objects.all().order_by('-id')[:5]
    data={
        "title":"ZenBlog | About",
        "Categories":Categories,
        "latestBlogData":latestBlogData,
    }
    return render(request,"about.html",data)

def contact(request):

    Categories=blog.objects.values('category').distinct()
    latestBlogData=blog.objects.all().order_by('-id')[:5]
    if request.method=="POST":
        try:
            if request.method=="POST":
                name=request.POST.get('name')
                email=request.POST.get('email')
                message=request.POST.get('message')
                subject=request.POST.get('subject')
                send_mail(
                    subject,
                    'Name: '+name+'\nMessage: '+message,
                    'sanketbhikajiugale@outlook.com',
                    [email],
                    fail_silently=False,
                )
                return render(request,"contact.html",{"title":"ZenBlog | Contact","submitted":True, "Categories":Categories, "latestBlogData":latestBlogData,})
        except:
            return render(request,"contact.html",{"title":"ZenBlog | Contact","submitted":False, "Categories":Categories, "latestBlogData":latestBlogData})
            
    else:

        data={
        "title":"ZenBlog | Contact",
        "Categories":Categories, 
        "latestBlogData":latestBlogData
            }
        return render(request,"contact.html",data)

def comment(request):
    if request.method=="POST":
        url=request.POST.get("url")
        name=request.POST.get("name")
        email=request.POST.get("email")
        date=datetime.now()
        message=request.POST.get("message")
        data=commentsModel(name=name, email=email, url=url, date=date, message=message)
        data.save()
        singleBlogData=blog.objects.get(url=url);
        commentsData=commentsModel.objects.filter(url=url);
        data={
                "title":"ZenBlog | Blog",
                "singleBlogData":singleBlogData,
                "commentsData":commentsData,
                # "headerCategory":headerCategory
        }       
    return render(request,'single-post.html',data)

def calculator(request):
    if request.method=="POST":
        result=''
        try:
            if request.method=="POST":
                value1=eval(request.POST.get('value1'))
                value2=eval(request.POST.get('value2'))
                operation=request.POST.get('operation')
                if operation=='+':
                    result= value1+value2
                elif operation=='-':
                    result=value1-value2
                elif operation=='/':
                    result=value1/value2
                elif operation=='*':
                    result=value1*value2
                else:
                    result="INVALID OPERATION"
                data2={
                    "title":"ZenBlog | Calculator",
                    "result":result,
                    "operation":'RESULT OF '+operation+" :",
                    "hidden":"text",
                    "value1":value1,
                    "value2":value2
                }
                return render(request,'calculator.html',data2)
        except:   
            return render(request,'calculator.html',{"result":"INVALID OPERATION"})
    else:    
        data1={
            "title":"ZenBlog | Calculator",
            "hidden":"hidden"
        }
        return render(request,'calculator.html',data1)