from django.shortcuts import render,redirect
from  .forms import AdminForm,CommentForm,ReplyForm
from . models import *
from django.core.paginator import Paginator,EmptyPage


# Create your views here.

# BLOG PAGE
def blog_page(request): 
    push = Post.objects.all().order_by('-date_posted')

    p = Paginator(push, 8)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context={
        'push':page,
    }

    return render(request,'blog/blog_page.html', context)


def category(request,id):
    category = Category.objects.get(id=id)
    post = Post.objects.filter(category = category)
    context={
        'title':category,
        'categorys':post
    }
    return render(request,'blog/blog_category.html',context)

# BLOG VIEW
def blog_view(request,id):
    user = request.user
    show = Post.objects.get(id=id)
    comments = Comment.objects.all().filter(post = show)
    form = CommentForm()
    rform = ReplyForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = show
            form.save()
            return redirect('blog_view',id)
    
    # reply
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply_id = request.POST.get('comment_id')
            rcomment = Comment.objects.get(id=reply_id)
            form = form.save(commit = False)
            form.comment = rcomment
            form.replier = request.user
            form.save()
            return redirect('blog_view',id)
        
    context={
        'push':show,
        'form':form,
        'comments':comments,
        'rform':rform,
        'user':user,
    }
    return render(request,'blog/blog_view.html', context)

def contact(request):  
    if request.method == "POST":
        fullname = request.POST['fullname'] 
        email = request.POST['email'] 
        gender = request.POST['gender'] 
        message = request.POST['message']

        insert = Contact(fullname=fullname,email=email,gender=gender,message=message)
        insert.save()
        return redirect('contact')
    return render(request,'blog/contact.html')

def blog_search(request):
 
    keyword = request.GET.get('my_search')
    source = Post.objects.filter(title__icontains = keyword)
    
    context = {
        'sources':source
    }

    return render(request,'blog/blog_search.html',context)

def updates(request):

    return render(request,'blog/updates.html')