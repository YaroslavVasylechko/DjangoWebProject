from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm

def news_home(request):
    news = Articles.objects.all() #.order_by('Date')[:4]
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Input text is incorrect'

    form = ArticlesForm()

    data = {
        'form': form
    }

    return render(request, 'news/create.html', data)