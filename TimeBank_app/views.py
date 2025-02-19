from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from TimeBank_app.models import Post, MainCategory, SubCategory
from TimeBank_account.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import re
from django.contrib import messages
from django.utils import timezone
# from .forms import PostForm, MsgForm
import json


# home
def index(request):
    return render(request, 'index.html')


# 거래글 목록
def post_list(request):
    # order_by : 순서정렬 / 최신순
    posts = Post.objects.all().order_by('-id')
    return render(request, 'post_list.html', {'posts': posts})




# 새 글 작성 페이지
def new_post(request):
    return render(request, 'new_post.html')



# 새 글 작성 POST
def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.date = request.POST['date']
        post.start_time = request.POST['start_time']
        post.end_time = request.POST['end_time']
        post.service = request.POST['service']
        post.location = request.POST['location']
        post.mainwork = request.POST['mainwork']
        post.subwork = request.POST['subwork']
        post.content = request.POST['content']
        post.author = request.user
        post.tok = request.POST['tok']
        post.status = '대기'
        post.save()
    return redirect('post_list')


# 자세히보기
def my_detail(request):
    return render(request, 'account.html')



# 대기->진행
def progress(request, post_id):
    post = Post.objects.get(pk = post_id)
    post.status = "진행"
    post.applicants = str(request.user)
    if post.service == "주고 싶어요":
        post.giver = str(post.author)
        post.taker = str(request.user)
    else:
        post.giver = str(request.user)
        post.taker = str(post.author)
    post.save()
    return redirect('post_list')


'''
#### AJAX ####
def post_ajax(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    user = request.user.username
    content = {'content':post.content, 'author':post.author.username, 'user': user}
    return HttpResponse(json.dumps(content), content_type="application/json")





# 진행
def progress_ajax(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    message = "신청완료"
    post.status = '진행'
    post.applicant = request.user.username
    post.save()
    content = {
        'post_status': post.status,
        'message': message,
        'applicant': request.user.username
    }
    return HttpResponse(json.dumps(content), content_type="application/json")
'''

'''
# 신규 거래 등록
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk)
            author = User.object.get(id=username)
            post = Post()
            post.content = form.cleaned_data['content']
            post.author = request.user
            post.service = request.service
            post.save()

            return redirect('/post/post_list/')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form':form})  
'''

'''
# 신청하기
@login_required
@require_POST
def send_msg(request):
    from_post = post.id
    pk = request.POST.get('pk')
    to_user = get_object_or_404(User, pk=pk)
    relation_created = Relation.objects.get_or_create(from_user=from_user, to_user=to_user)

    if created:
        message = '팔로우 시작!'
        status = 1

    return render('post_list.html')
'''
    



'''
# 신청 내용 저장
def create_message(request):  
    posts = Post.objects.get(pk=post.id)
    try:
    # user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
        message = MessageItem.objects.get(post_id=post.id, user__id=request.user.pk)
        if message:
            if message.post.id == post.id:
                message.message_list += 1
                message.save()
    except MessageItem.DoesNotExist:
        user = User.objects.get(pk=request.user.pk)
        message = MessageItem(
            user=user,
            post=post,
            message_list=1,
        )
        message.save()
    return redirect('account')
#        return render(request, 'post_list.html', {'posts': posts})
'''









#########
'''
class ButtonView:
    def __init__(self, show_btn):
        self.show_btn = show_btn

    def applicant_mode()
    pass
'''


'''
# 신청하기
#@login_required(login_url='login')
def send_message(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author != request.user:
        try:
            # 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
            message = MessageItem.objects.get(post_id=post.pk, user__id=request.user.pk)
            if message:
                if message.post.content == post.content:
                    message.quantity += 1
                    message.save()
        except MessageItem.DoesNotExist:
            user = User.objects.get(pk=request.user.pk)
            message = MessageItem(
                user=user,
                post=post,
                message_list=1,
            )
            message.save()
        return redirect('profile')
    else:
        messages.error(request, '자신의 글은 신청할 수 없습니다.')
 '''       



'''
# 신규 거래 등록 - 템플릿 보여주기
@login_required
def new(request):
    posts = Post.objects.all
    return render(request, 'new_post.html', {"posts":posts})

# 거래등록 - 데이터 저장
def create(request):
    
    start_time = request.GET["start_time"]
    end_time = request.GET["end_time"]
    service = request.GET["service"]
    location = request.GET["location"]
    main_work = request.GET["main_work"]
    sub_work = request.GET["sub_work"]
    content = request.GET["content"]
    
    post.start_time = start_time
    post.end_time = end_time
    post.start_time = start_time
    post.service = service
    post.location = location
    post.main_work = main_work
    post.sub_work = sub_work
    
    post.content = content
    post.time = timezone.now()
    post.save()
    return redirect('post_list')
    '''




        