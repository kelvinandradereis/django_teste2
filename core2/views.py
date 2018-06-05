from django.shortcuts import render,redirect
from core2.models import Post
from core2.forms import PostForm


def home(request):
    return render(request, 'core2/index.html')


def lista(request):
    lista = Post.objects.all().order_by('-id')
    return render(request,'core2/lista.html', {'lista_posts':lista})

def novo(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return redirect(lista)

    return render(request,'core2/novo.html',{'form':form})

# Create your views here.
