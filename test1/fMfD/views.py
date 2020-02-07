# fMfD/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world!")

def detail(request):
    comments_list = Comments.objects.order_by('-pub_date')[:10]
    context = {'comments_list': comments_list}
    return render(request, 'fMfD/detail.html', context)

def addComments(request):
    if request.method == 'POST':
        temp_content = request.POST['content']
    temp_comments = Comments(content=temp_content, pub_date=timezone.now())
    temp_comments.save()
    # 重定向
    return HttpResponseRedirect(reverse('detail'))
def delComments(request, comments_id):
    commentsID = comments_id
    Comments.objects.filter(id=commentsID).delete()
    return HttpResponseRedirect(reverse('detail'))