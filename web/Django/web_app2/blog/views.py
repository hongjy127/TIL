from decimal import Context
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView 
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import FileResponse
from django.conf import settings
from django.utils import timezone

import os

from blog.models import Post, PostAttachFile
from blog.forms import PostSearchForm
from mysite.views import OwnerOnlyMixin

# Create your views here.

# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDV(DetailView):
    model = Post

    # 다른사람 게시글만 볼 때 업그레이드     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        
        if self.request.user != self.object.owner:  #소유자인지 확인
            self.object.read_cnt += 1
            self.object.save()
            
        return context

# ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'

# Tag View
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

# FormView
# 만약 pagination을 하고싶다면 ListView도 상속해서 다중상속 이용하면 됨.
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(
            Q(title__icontains=searchWord) |
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)
        ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        # form.instance.modify_dt = timezone.now()
        
        response = super().form_valid(form) # Post 모델 저장, self.object
        # 업로드 파일 얻기
        files = self.request.FILES.getlist("files")
        print(files)
        for file in files:
            attach_file = PostAttachFile(post= self.object, filename = file.name,
                                        size = file.size, content_type = file.content_type,
                                        upload_file = file)
            attach_file.save()
        return response

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('blog:index')


# 파일 다운로드
def download(request, id):
    file = PostAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))

    return FileResponse(open(file_path, 'rb'))

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:index')
    
    def form_valid(self, form):
        # form.instance.modify_dt = timezone.now()

        # 삭제
        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files: # fid는 문자열 타입임
            file = PostAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path) # 실제 파일 삭제
            file.delete() # 모델 삭제(테이블의 행 삭제)

        # 추가 업로드
        response = super().form_valid(form)
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = PostAttachFile(post= self.object, filename = file.name,
                                        size = file.size, content_type = file.content_type, upload_file = file)
            attach_file.save()
        
        return response