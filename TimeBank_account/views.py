from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import auth
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.http import HttpResponse
from django.contrib import messages
from TimeBank_app.models import Post, Register
from .models import User
import json


# 홈화면
def index(request):
    return render(request, 'index.html')



# 회원가입
def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        name = request.POST["name"]
        password = request.POST["password"]
        password_check = request.POST["pw_check"]
        #image = request.FILES["image"]

        #text output
        #f = open("tmp.txt", 'w')
        #data = '{}\n {}\n {}\n{}\n{}\n{}\n'.format( userid, email, username, password, password_check, image)
        #f.write(data)
        #f.close()

        # 비밀번호 재확인 불일치
        if password != password_check:
            return render(request, "register.html")
        # 새로운 유저 생성
        user = User.object.create_user(username=username, email=email, password=password, name=name)
        auth.login(request, user)
    return redirect('index')

# 로그인
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        # 존재하지 않는 user
        if user is None:
            return render(request, "login.html", {"msg": "로그인 실패!"})
        # 로그인 처리
        auth.login(request, user)
    return redirect('index')


# 로그아웃
def logout(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            auth.logout(request)
    return redirect('index')



# 프로필
@login_required
def profile(requset,username):
    user = get_object_or_404(User,username=username)
    return render(requset, "profile.html", {"user_profile":user, 'username': username})


# 계좌 내역 보여주기
def account_history(request):
    posts = Post.objects.all()
    # 내가 등록한 거래
    my_posts = posts.filter(author = request.user)
    # 내가 신청한 거래
    regsiter_posts = posts.filter(applicants = request.user)
    return render(request, "account.html", {'my_posts': my_posts, 'regsiter_posts': regsiter_posts})


# 잔액 조회
@login_required
def balance(request):
    post = Post.objects.all()
    user = request.user
    success = post.filter(status = "완료") 
    success_posts = success.filter(author = request.user) | success.filter(applicants = request.user)
    plus_toks = success_posts.filter(service = "주고싶어요") & success_posts.filter(author = request.user)
    minus_toks = success_posts.filter(service = "받고싶어요") & success_posts.filter(author = request.user)
    return render(request, "balance.html", {'success_posts': success_posts, 'user':user, 'plus_toks':plus_toks, 'minus_toks':minus_toks})

    



# 내가 쓴 글 자세히보기
def my_post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.status == "진행" and post.service == "주고싶어요":
        if post.author == request.user:
            btn_msg = "승인대기"
        elif post.author != request.user:
            btn_msg = "완료하기"
    elif post.status == "진행" and post.service == "받고싶어요":
        if post.author == request.user:
            btn_msg = "완료하기"
        elif post.author != request.user:
            btn_msg = "승인대기"
    return render(request, "my_post_detail.html", {'post':post, 'btn_msg':btn_msg})


# 진행-> 완료하기
def success(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.status = "완료"
        post.save()
    return redirect("my_post_detail")


# 내가 신청한 거래 자세히보기
def my_register_detail(request, post_id):
    register_post = Post.objects.get(pk=post_id)
    return render(request, "my_register_detail.html", {"register_post":register_post})
