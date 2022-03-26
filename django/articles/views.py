from django.shortcuts import render
from .models import Article

# Create your views here.
def articles_detail_view(request,id=None):
    article_obj=None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context={
        "object": article_obj
    }
    return render(request,"articles/detail.html",context=context)

def articles_search_view(request):
    print(request.GET)
    query_dict=request.GET
    query=query_dict.get("query")
    article_obj=None
    if query is  not None:
        article_obj = Article.objects.get(id=query)
    context={
         "object": article_obj
    }
    return render(request,"articles/search.html",context=context)

def articles_create_view(request,id=None):
    
    context={}
    
    return render(request,"articles/create.html",context=context)