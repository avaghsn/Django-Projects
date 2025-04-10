from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from .forms import TicketForm, CommentForm, SearchForm, CreatePostForm
from .models import Post, Ticket, Image
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from django.contrib.auth.decorators import login_required


# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/list.html"


class PostDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blog/detail.html', context)


def index(request):
    return render(request, 'blog/index.html')


def ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = Ticket.objects.create()
            cleaned_data = form.cleaned_data
            ticket_obj.message = cleaned_data['message']
            ticket_obj.name = cleaned_data['name']
            ticket_obj.email = cleaned_data['email']
            ticket_obj.phone = cleaned_data['phone']
            ticket_obj.subject = cleaned_data['subject']
            ticket_obj.save()
            return redirect('blog/index')
    else:
        form = TicketForm()
    return render(request, "forms/ticket.html", {'form': form})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    context = {
        'post': post,
        'comment': comment,
        'form': form,
    }
    return render(request, "forms/comment.html", context)


def post_search(request):
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results1 = (Post.published.annotate(similarity=TrigramSimilarity('title', query)).filter(
                similarity__gt=0.1).order_by('-similarity'))
            results2 = (Post.published.annotate(similarity=TrigramSimilarity('description', query)).filter(
                similarity__gt=0.1).order_by('-similarity'))

            results = (results1 | results2).order_by('-similarity')

    context = {
        'query': query,
        'results': results
    }
    return render(request, 'blog/search.html', context)


def profile(request):
    user = request.user
    posts = Post.published.filter(author=user)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'blog/profile.html', context)


@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            Image.objects.create(image_file=form.cleaned_data['image1'], post=post)
            Image.objects.create(image_file=form.cleaned_data['image2'], post=post)
            return redirect('blog:profile')
    else:
        form = CreatePostForm()
    return render(request, 'forms/create-post.html', {'form': form})
