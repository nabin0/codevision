from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.

def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about us.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        contact = Contact(name=name, email=email, phone=phone,msg=msg)
        contact.save()
        messages.info(request, "Thanks For contacting us. We will reach to you soon.")
    return render(request, "home/contact us.html")


def search(request):
    query = request.GET['query']
    if len(query) > 50:
        allPosts = Post.objects.none()
    else:
        postsByTitle = Post.objects.filter(title__icontains=query);
        postsByContent = Post.objects.filter(content__icontains=query);
        allPosts = postsByTitle.union(postsByContent)

    if allPosts.count() == 0:
        messages.warning(request, "No Search Result found please check your keyword and try again.")
    contex = {"allPosts": allPosts, "query":query}
    return render(request, "home/search.html", contex)