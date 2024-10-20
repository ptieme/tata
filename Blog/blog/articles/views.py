from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse  

from .forms import ArticleForm

from .models import Article

def articles_view(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'articles/list.html', context={'articles': articles})

def article_view(request, slug):
    article = get_object_or_404(Article,slug=slug)
    return render(request, 'articles/detail.html', context={"article": article})










    # try:
    #  article = Article.objects.get(slug=slug)
   
    #  return render(request, 'articles/detail.html', context={"article": article})
    # except Article.DoesNotExist:
    #    raise  Http404("L'article nexiste pas")


def creer_view(request):
    form  =ArticleForm()
    if request.method == 'POST':
        form=ArticleForm(request.POST ,request.FILES) # on recupere ce qui est entre dans notre methode post
        form.save()
        return HttpResponseRedirect(reverse('articles:articles')) # une fois les donner sauvegarder redirige lutilisateur sur la page article
    return render(request,'articles/creer.html', context ={'form':form} )