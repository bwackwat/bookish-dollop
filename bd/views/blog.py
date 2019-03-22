from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from bd.models import Blog


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


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/view.html'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'description', 'style')
    template_name = 'blogs/form.html'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')
    template_name = 'blogs/confirm_delete.html'
