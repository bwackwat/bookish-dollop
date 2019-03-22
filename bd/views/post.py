from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views import View

from bd.models import Post, Blog


class PostListView(View):

    def get(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        posts = Post.objects.filter(blog=blog).order_by('-created')

        return render(request, 'posts/list.html', {
            'blog': blog,
            'posts': posts,
        })


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content')
    template_name = 'posts/form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.blog = get_object_or_404(Blog, id=self.kwargs['blog_id'])
        post.owner = self.request.user
        post.save()
        return redirect('posts', blog_id=self.kwargs['blog_id'])


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/view.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content')
    template_name = 'posts/form.html'

    def get_success_url(self):
        return reverse_lazy('posts', kwargs={'blog_id': self.object.blog.id})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('posts', kwargs={'blog_id': self.object.blog.id})