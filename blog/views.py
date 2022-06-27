from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from tags.models import TaggedItem
from .models import Post, Category, Comment
from tags.models import Tag
from .forms import AddPostForm, EditPostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import logging


# logger = logging.getLogger(__name__)


def category_post_view(request, cat):
    cat_posts = list(Post.objects.select_related('category').filter(category=cat))
    for post in cat_posts:
        print(post.id)
    context = {'posts': cat_posts, 'cat': cat}
    return render(request, 'blog/cat_post.html', context)


class PostView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 5

    def get_queryset(self, **kwargs):
        queryset = Post.objects.filter(approved=True)
        return queryset



class TagPostView(ListView):
    model = Post
    template_name = 'blog/tag_post.html'
    paginate_by = 5

    def get_queryset(self,**kwargs):
        tagged_items = TaggedItem.objects.filter(tag_id=self.kwargs.get('tag_id'))
        post_ids = [tagged_item.object_id for tagged_item in tagged_items]
        post_objects = Post.objects.filter(id__in=post_ids, approved=True)
        return post_objects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_label'] = get_object_or_404(Tag, id=self.kwargs.get('tag_id')).label
        return context




class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    form = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        liked = False
        if post.likes.filter(id= self.request.user.id):
            liked = True
        context['liked'] = liked
        context['post_detail'] = post
        return context


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = "blog/add_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.is_superuser:
            form.instance.approved = True
            return super(AddPostView, self).form_valid(form)
        else:
            super(AddPostView, self).form_valid(form)
            return redirect('blog:post-submit')



class PostSubmitView(TemplateView):
    template_name = 'blog/post_submit.html'



class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "blog/update_post.html"



class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('blog:index')


class CategoryPostView(ListView):
    model = Post
    template_name = 'blog/cat_post.html'
    paginate_by = 5

    def get_queryset(self,**kwargs):
        queryset = Post.objects.select_related('category').filter(category=self.kwargs.get('cat'), approved=True)
        return queryset

    def get_context_data(self, **kwargs):
        print(self.kwargs.get('cat'))
        category_obj = Category.objects.filter(id=self.kwargs.get('cat')).first()
        context = super().get_context_data(**kwargs)
        context['category_name'] = category_obj.name
        return context


def submit_comment_view(request, slug):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            print(slug)
            post = get_object_or_404(Post, slug=slug)
            print(type(post))
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post', slug)

    
def post_search_view(request):
    query_dict = request.GET
    query_text = query_dict.get("search_query")   
    queryset = Post.objects.search(query_text)
    if queryset:
        context = {'posts': list(queryset)}
        return render(request, "blog/search_post.html", context)
    else:
        return redirect('blog:index')



def like_post_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog:post', args=[str(post.slug)]))