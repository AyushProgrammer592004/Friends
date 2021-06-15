from django.shortcuts import render, HttpResponse, redirect
from home.models import Friend
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(redirect_field_name='', login_url='/login')
def home(request):
    if request.method == 'POST':
        friendname = request.POST['friendname']
        user = request.user

        friend = Friend(name=friendname, user=user)
        friend.save()
        return redirect('/')
    log_user = request.user
    friends = Friend.objects.filter(user=log_user) 
    context = {
        "friends": friends
    }
    return render(request, 'home.html', context)

def deletefriend(request, sno):
    delFriend = Friend.objects.filter(sno=sno).first()
    delFriend.delete()
    return redirect('/')

def updatefriend(request, sno):
    if request.method == 'POST':
        friendname = request.POST['friendname']

        friend = Friend.objects.filter(sno=sno).first()
        friend.name = friendname
        friend.save()
        return redirect('/')
    friend = Friend.objects.filter(sno=sno).first()
    context = {
        "friend": friend
    }
    return render(request, 'update.html', context)

def signupUser(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        cpass = request.POST['cpass']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('/')
    return render(request, 'signup.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')