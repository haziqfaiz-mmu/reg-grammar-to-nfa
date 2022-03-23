""" 
To render html web pages
 """
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

def article_home_view(request):
    return HttpResponse
def home_view(request,*args, **kwargs):
    """ 
    Take in a reqest (Django sends request)
    Return HTML as response
    """
    name = "Haziq"
    article_obj = Article.objects.get(id=2)
    article_queryset = Article.objects.all()
   
    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id
    }
    HTML_STRING = render_to_string("home-view.html",context = context)
    
    return HttpResponse(HTML_STRING)
