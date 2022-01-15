from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from app.models import signup,blog
from app.forms import CommentForm,Blogform
# Create your views here.
def signup1(request):
    if request.method == "POST":
        Realname = request.POST['realname']
        Username = request.POST['username']
        sEmail = request.POST['semail']
        sPassword = request.POST['spassword']

        if User.objects.filter(username=Username).exists():
            messages.info(request, "user exists")
            return redirect("/")
        else:
            user = User.objects.create_user(username=Username, email=sEmail, password=sPassword, first_name=Realname)
            user.save()
            auth.login(request, user)
            print("user made")
            return redirect("/")

    else:
        form1 = signup.objects.all()
        return render(request, 'Signup.html', {'signup': form1})



def login(request):
    if request.method == "POST":
        username =request.POST['lgusername']
        password =request.POST['lgpassword']
        user =auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid username or password")
            return redirect("/login")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def blog1(request):
    blogs= blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})
def blogdetail(request ,slug):
    post =blog.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request,'blog_detail.html',{'post':post ,'form': form})


def writeblog(request):
    if request.method == "POST":
        form=Blogform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form=Blogform()
        return render(request,"write.html",{'form':form})
