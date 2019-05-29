from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404,redirect
from .models import PostArticles
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,DetailView
from .update_form import UpdateForm
# Create your views here.
def login_view(request):
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return render(request,'login.html')


def about_view(request):
    return render(request,'about.html')

def crud_view(request):
    post = PostArticles.objects.all()
    pdic = {'pkey': post}
    return render(request, 'Admin.html', pdic)


def createpost(request):
        if request.method=='POST':
            title = request.POST.get('title')
            author = request.POST.get('slug').upper()
            slug=request.POST.get('slug')
            images = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(images.name, images)
            published_date=request.POST.get('published_date')
            description=request.POST.get('description')
            postArticles=PostArticles(title=title,author=author,slug=slug,image=images,published_date=published_date,description=description)

            postArticles.save()

        return render(request, 'post_articles.html')


def displaypost(request):
    post_obj=PostArticles.objects.all().order_by('-published_date')
    post_dict={'post_key':post_obj}
    return render(request,'index.html',post_dict)


def deleteView(request, id):
    postArticles = get_object_or_404(PostArticles, pk=id)
    postArticles.delete()
    return redirect('crud') # {'object':postArticles}

class DetailPostArticles(DetailView):
    model = PostArticles
    def get(self, request, *args, **kwargs):
        articles = get_object_or_404(PostArticles, pk=kwargs['pk'])
        context={'article':articles}
        return render(request,'detail_articles.html',context)



class UpdatePostArticle(UpdateView):
    model = PostArticles
    fields = ('title','author','slug','image','published_date','description')
    context_object_name = 'postArticle'
    template_name = 'update_articles.html'
    def form_valid(self, form):
        form.save()
        return redirect('crud')
