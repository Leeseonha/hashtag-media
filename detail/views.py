from django.shortcuts import get_object_or_404, render, redirect
from .forms import DetailForm,CommentForm, HashtagForm, MediaForm
from .models import Detail,Comment, Hashtag
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.conf.urls.static import static
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

def index(request):
        return render(request, 'index.html')

def layout(request):
        medias = Detail.objects
        return render(request, 'layout.html',{'medias':medias})

# comment생성
def detail(request, pk):
        detail = get_object_or_404(Detail , id=pk)
        if request.method == "POST":
                form = CommentForm(request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.post = detail
                        comment.comment_text = form.cleaned_data["comment_text"]
                        comment.save()
                        return redirect("detail", pk)
        else:
                form = CommentForm()
                return render(request, "detail2.html", {"detail":detail, "form":form})

# 페이지를 생성하기 위한 함수입니다.
def new(request):
        return render(request,'new.html')
                  
def create(request, detail=None):
        if request.method =='POST':
                form = DetailForm(request.POST,request.FILES,instance=detail)
                if form.is_valid():
                        detail = form.save(commit=False)
                        detail.pub_date=timezone.now()
                        detail.save()
                        form.save_m2m()
                        return redirect('home2')
        else:
                form = DetailForm(instance=detail)
                return render(request, 'new.html', {'form':form})  

def update(request, board_id):
        detail = Detail()
        detail.title = request.GET['title']
        detail.content = request.GET['content']
        detail.pub_date = timezone.datetime.now()
        detail.save()
        return redirect('/detail/')

def home2(request):
        details = Detail.objects
        hashtags = Hashtag.objects
        return render(request, 'home2.html',{'details' :details,'hashtags':hashtags})

def edit(request,pk):
        detail=get_object_or_404(Detail,pk=pk)
        return create(request,detail)

def remove(request,pk):
        detail=get_object_or_404(Detail,pk=pk)
        detail.delete()
        return redirect('home2')
        
def comment_edit(request,detail_id, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if request.method=='POST':
                form=CommentForm(request.POST,instance=comment)
                if form.is_valid():
                        comment=form.save()
                        return redirect('detail', detail_id)
        else:
                form=CommentForm(instance=comment)
                return render(request,'detail2.html',{'form':form})

def comment_remove(request,detail_id,pk):
        comment=get_object_or_404(Comment, pk=pk)
        comment.delete()
        return redirect('detail', detail_id)

def hashtagform(request, hashtag=None):
        if request.method == 'POST':
                form = HashtagForm(request.POST, instance=hashtag)
                if form.is_valid():
                        hashtag = form.save(commit=False)
                        if Hashtag.objects.filter(name=form.cleaned_data['name']):
                                form = HashtagForm()
                                error_message = "이미 존재하는 해시태그 입니다."
                                return render(request, 'hashtag.html',{'form':form,'error_message':error_message})
                        else:
                                hashtag.name = form.cleaned_data['name']
                                hashtag.save()
                        return redirect('home2')
        else:
                form = HashtagForm(instance=hashtag)
                return render(request, 'hashtag.html',{'form':form})

def search(request, hashtag_id):
        hashtag = get_object_or_404(Hashtag,pk=hashtag_id)
        return render(request, 'search.html',{'hashtag':hashtag})