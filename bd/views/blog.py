from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views import View

from bd.models import *


class JsonView(View):

    def get(self, request):
        return HttpResponse('result')

    def post(self, request):
        return HttpResponse('result')

    def put(self, request):
        return HttpResponse('result')

    def delete(self, request):
        return HttpResponse('result')


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blogs/list.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'description', 'style')
    template_name = 'blogs/form.html'

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.owner = self.request.user
        blog.save()
        return redirect('blogs')


class BlogDetailView(View):

    def get(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        posts = Post.objects.filter(blog=blog).order_by('-created')

        return render(request, 'blogs/view.html', {
            'blog': blog,
            'posts': posts,
        })


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'description', 'style')
    success_url = reverse_lazy('blogs')
    template_name = 'blogs/form.html'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')
    template_name = 'blogs/confirm_delete.html'
